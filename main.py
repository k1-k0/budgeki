import uvicorn
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

import crud
import models
import schemas
from database import engine, SessionLocal


print("Create db models")
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.create_user(db=db, user=user)


@app.get('/users/', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not exists')
    return user


@app.get('/users/', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not exists')
    return user


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=42000)