from fastapi import FastAPI, status, HTTPException, Depends
from db import metadata, database, engine, Users
from schemas import User, UserUpdate
from Token import get_current_user, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import pbkdf2_sha256

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/users/")
async def get_users(current_user: User = Depends(get_current_user)):
    query = Users.select()
    return await database.fetch_all(query=query)


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def get_users(user: User):
    hashed_pass = pbkdf2_sha256.hash(user.password)
    query = Users.insert().values(username=user.username, roles=user.roles, password=hashed_pass)
    await database.execute(query)
    return {**user.dict()}


@app.post("/login", status_code=status.HTTP_202_ACCEPTED)
async def login(request: OAuth2PasswordRequestForm = Depends()):
    query = Users.select().where(Users.c.username == request.username)
    myuser = await database.fetch_one(query=query)
    if not myuser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    if not pbkdf2_sha256.verify(request.password, myuser.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="password is invalid")
    acccess_token = create_access_token(
        data={"sub": myuser.username}
    )
    return {"access_token": acccess_token, "token_type": "bearer"}


@app.put("/users/", status_code=status.HTTP_205_RESET_CONTENT)
async def update_user(id: int, user: UserUpdate):
    if user.username is not None:
        query = Users.update().where(Users.c.id == id).values(username=user.username)
        await database.execute(query)
    if user.password is not None:
        hashed_pass = pbkdf2_sha256.hash(user.password)
        query = Users.update().where(Users.c.id == id).values(password=hashed_pass)
        await database.execute(query)
    if user.roles is not None:
        query = Users.update().where(Users.c.id == id).values(roles=user.roles)
        await database.execute(query)
    return {**user.dict()}


@app.delete("/users/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
    query = Users.delete().where(Users.c.id == id)
    await database.execute(query)
    return {"messeage": "user deleted successfully !"}
