from pydantic import BaseModel

dct = {
    "name": "step", 
    "age": 22
}


class Obj(BaseModel):
    name: str
    age: int

obj = Obj(name="step", age=22)

for key, value in obj.model_dump().items():
    print()
