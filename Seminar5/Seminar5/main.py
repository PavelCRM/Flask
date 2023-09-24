from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modules.user import User, get_user_by_id, add_user, update_user, delete_user
from djinja import Djinja

app = FastAPI()
djinja = Djinja(app)


class UserInDB(BaseModel):
    id: int
    name: str
    email: str
    password: str


@app.post("/users/", response_model=UserInDB)
def create_user(user: UserInDB):
    return add_user(user)


@app.put("/users/{user_id}", response_model=UserInDB)
def modify_user(user_id: int, user: UserInDB):
    existing_user = get_user_by_id(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(user_id, user)


@app.delete("/users/{user_id}", response_model=UserInDB)
def remove_user(user_id: int):
    existing_user = get_user_by_id(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return delete_user(user_id)


@app.get("/users/{user_id}", response_model=UserInDB)
def get_user(user_id: int):
    existing_user = get_user_by_id(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return existing_user


@app.get("/users/", response_model=list[UserInDB])
def get_all_users():
    return User.users


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
