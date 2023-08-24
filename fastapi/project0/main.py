from fastapi import FastAPI, HTTPException
from models import *

app = FastAPI()

db: List[User] = [
    User(
        id="b6ef0fce-bcf9-4414-9ee0-371b5bac07cc",
        full_name="amin salehi",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id="28e48a09-706c-40c2-a639-269a36b36fbf",
        full_name="mary jane",
        gender=Gender.custom,
        roles=[Role.user]
    ),
    User(
        id="419b409b-51e8-4f1c-8456-0d5e0fe50f43",
        full_name="hannaneh gholami",
        gender=Gender.female,
        roles=[Role.vip]
    ),
]


@app.get("/users")
async def fetch_users():
    return db


@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return {"user added": user}


@app.delete("/users")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} Not Found"
    )


@app.put("/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.full_name is not None:
                user.full_name = user_update.full_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} Not Found"
    )
