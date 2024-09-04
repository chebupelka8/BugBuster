
"""
FROM USER:
    {
        code: str,
        callable_name: str
    }
"""


with open("./input_code.py", "r", encoding="utf-8") as file:
    input_code = file.read()


exec(input_code)



from typing import Callable, Any
from functools import wraps

from pydantic import BaseModel

import json
import subprocess


class ResultType(BaseModel):
    stdout: str
    stderr: str
    return_code: int


class Test:
    def __init__(self) -> None:
        self.test_cases = []

    def launch_code(self, code: str, callable_name: str, *params) -> ResultType:
        result = subprocess.run(["python", "-c", code + f"\n{callable_name}{str(params)}"], text=True, capture_output=True)

        return ResultType(
            stdout=result.stdout,
            stderr=result.stderr,
            return_code=result.returncode
        )
    
    def generate_testcase_output(self, message: str, is_completed: bool, result: ResultType) -> dict:
        return {
            "message": message,
            "is_completed": is_completed,
            "return_code": result.return_code,
            "output": result.stdout
        }

    def check_output(self, func: Callable, expected_output: Any, *params) -> None:
        try:
            launched = self.launch_code(input_code, "target_function", *params)

            if not func(*params) == expected_output:
                self.test_cases.append(
                    self.generate_testcase_output(
                        f"For {params} should return {expected_output}", 
                        False,
                        launched
                    )
                )
            else:
                self.test_cases.append(
                    self.generate_testcase_output(
                        "Ok", 
                        True,
                        launched
                    )
                )

        except BaseException as error:
            self.test_cases.append(
                self.generate_testcase_output(
                    str(error),
                    False,
                    launched
                )
            )

    def basic_test(self) -> Callable:
        def inner(func: Callable) -> Callable:

            @wraps(func)
            def wrapper(*args, **kwargs) -> dict:
                try:
                    func(*args, **kwargs)
                
                except BaseException as error:
                    print(error)
                
                return {
                    "is_completed": all(map(lambda entry: entry["is_completed"], self.test_cases)),
                    "test_cases": self.test_cases
                } 

            return wrapper
        return inner


test = Test()

@test.basic_test()
def checker_function():
    test.check_output(target_function, 101, "str", "str")  # type: ignore
    # test.check_output(target_function, 5, "str", "str")  # type: ignore
    # test.check_output(target_function, 1, "str", "str")  # type: ignore


print(json.dumps(checker_function(), indent=4))
