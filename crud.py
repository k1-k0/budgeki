import models
import schemas

from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int) -> schemas.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> schemas.User:
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User:
    fake_hashed_password = user.hashed_password + 'hash'    # FIXME: hash password
    db_user = models.User(email=user.email, hached_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user