from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



from pydantic import BaseModel

class User(BaseModel):
    
    name: str
    email: str
    password: str

@app.post("/users/")
def create_user(user: User):
    return {"name": user.name, "email": user.email, "password": user.password}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    return {"user_id": user_id, "user": user}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"user_id": user_id, "status": "deleted"}


@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}