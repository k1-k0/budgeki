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


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=42000)