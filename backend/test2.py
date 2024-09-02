import subprocess


with open("./input_code.py", "r", encoding="utf-8") as file:
    input_code = file.read()



callable_name = "target_function"
params = ("asldkfjasd", "sadfasdf", "asdf")
result = subprocess.run(["python", "-c", input_code + f"\n{callable_name}{str(params)}"], text=True, capture_output=True)



print(
    input_code + f"\n{callable_name}{str(params)}",
    result.stderr
)
