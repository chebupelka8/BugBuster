from typing import List


def target_function(string: str) -> List[int]:
    return [
        int(char) for char in string if char.isdigit()
    ]



class InvalidOutput(ValueError):
    ...


from typing import Callable, Any
from functools import wraps


class Test:

    @staticmethod
    def check_output(func: Callable, expected_output: Any, *args) -> None:
        if not func(*args) == expected_output:
            raise InvalidOutput(f"For {args} should return {expected_output}")

    @classmethod
    def basic_test(cls) -> Callable:
        def inner(func: Callable) -> Callable:

            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                print("Basic Tests")

                try:
                    func(*args, **kwargs)
                
                except BaseException as error:
                    if isinstance(error, InvalidOutput):
                        print(str(error))
                    
                    else:
                        raise error

            return wrapper
        return inner


@Test.basic_test()
def checker_function():
    Test.check_output(target_function, [1, 2, 3], "af1asd23adf")
    Test.check_output(target_function, [1, 2, 4], "af1asd23adf")


checker_function()
