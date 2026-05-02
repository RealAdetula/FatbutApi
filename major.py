from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

class Student(BaseModel):
    name: str
    age: int
    gender: str
    grade: str
@app.post("/Create_student")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "gender": student.gender,
        "grade": student.grade
    }
@app.get("/get_student")
def get_student():
    return {
        "name": "John Doe",
        "age": 20,
        "gender": "Male",
        "grade": "A"
    }




