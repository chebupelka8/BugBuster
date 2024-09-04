from typing import Callable, Any
from functools import wraps

from pydantic import BaseModel

import subprocess
import os

from contextlib import redirect_stdout


class ResultType(BaseModel):
    stdout: str
    stderr: str
    return_code: int


class Test:

    def __init__(self, input_code: str) -> None:
        self.test_cases = []
        self.input_code = input_code
    
    def launch_code(self, callable_name: str, *params) -> ResultType:
        result = subprocess.run(["python", "-c", self.input_code + f"\n{callable_name}{str(params)}"], text=True, capture_output=True)

        return ResultType(
            stdout=result.stdout,
            stderr=result.stderr,
            return_code=result.returncode
        )
    
    def add_test_case(self, message: str, is_completed: bool, result: ResultType) -> None:
        self.test_cases.append(
            {
                "message": message,
                "is_completed": is_completed,
                "return_code": result.return_code,
                "output": result.stdout
            }
        )

    def check_output(self, callable_name: str, expected_output: Any, *params) -> None:
        launched = self.launch_code(callable_name, *params)

        try:
            if callable_name in globals():
                with open(os.devnull, 'w') as fnull:
                    with redirect_stdout(fnull):
                        function_result = globals()[callable_name](*params)  # run function without output

                if function_result == expected_output:
                    self.add_test_case(
                        "Ok", 
                        True,
                        launched
                    )

                else:
                    self.add_test_case(
                        f"For {params} should return {expected_output}", 
                        False,
                        launched
                    )
            
            else: 
                raise ValueError("Invalid callable name")
        
        except BaseException as error:
            self.add_test_case(
                str(error),
                False,
                launched
            )
    
    def basic_tests(self) -> Callable:
        def inner(func: Callable[..., None]) -> Callable:

            @wraps(func)
            def wrapper(*args, **kwargs) -> dict:
                func(*args, **kwargs)

                return {
                    "is_completed": all(map(lambda entry: entry["is_completed"], self.test_cases)),
                    "test_cases": self.test_cases
                } 
            
            return wrapper
        return inner

