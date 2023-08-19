from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/")
async def get_user(db: Session = Depends(get_db)):
    all_user = db.query(models.User).all()
    return all_user


@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def register_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(id=user.id, email=user.email, password=user.password, roles=user.roles)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.put("/user/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(user_id, user_update: schemas.UserUpdateRequest, db: Session = Depends(get_db)):
    available_id = db.query(models.User).filter(models.User.id == user_id)
    counter = 0
    for i in available_id:
        counter += 1
    if counter != 0:
        if user_update.email is not None:
            available_id.update({'email': user_update.email})
        if user_update.password is not None:
            available_id.update({'password': user_update.password})
        if user_update.roles is not None:
            available_id.update({'roles': user_update.roles})
        db.commit()
        return {"message": " data is updated"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} Not Found"
    )


@app.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id, db: Session = Depends(get_db)):
    available_id = db.query(models.User).filter(models.User.id == user_id)
    counter = 0
    for i in available_id:
        counter += 1
    if counter != 0:
        available_id.delete(synchronize_session=False)
        db.commit()
        return {"message": " user is deleted"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} Not Found"
    )
