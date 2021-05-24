from typing import List, Optional
import models
import schemas

from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int) -> schemas.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> schemas.User:
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User:
    fake_hashed_password = user.password + 'hash'    # FIXME: Remove simulation of hash password
    db_user = models.User(name=user.name, email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.User) -> schemas.User:
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    if db_user.name != user.name:
        db_user.name = user.name
    if db_user.email != user.email:
        db_user.email = user.email
    for account in user.accounts:
        if account not in db_user.accounts:
            db_user.append(account)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_account(db: Session, account: schemas.AccountCreate, user_id: int) -> schemas.Account:
    db_account = models.Account(name=account.name, value=account.value, user_id=user_id)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_account(db: Session, account_id: int) -> schemas.Account:
    return db.query(models.Account).filter(models.Account.id == account_id).first()


def get_user_accounts(db: Session, user_id: int) -> List[schemas.Account]:
    return db.query(models.Account).filter(models.Account.user_id == user_id).first()


def create_group(db: Session, group: schemas.GroupCreate, user_id: int) -> schemas.Group:
    db_group = models.Group(name=group.name, user_id=user_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def get_group(db: Session, group_id: int) -> schemas.Group:
    return db.query(models.Group).filter(models.Group.id == group_id).first()


def get_user_groups(db: Session, user_id: int) -> List[schemas.Group]:
    return db.query(models.Group).filter(models.Group.user_id == user_id).all()


def create_category(db: Session, category: schemas.CategoryCreate, group_id) -> schemas.Category:
    db_category = models.Category(name=category.name, group_id=group_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, category_id: int) -> schemas.Category:
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_group_categories(db: Session, group_id: int) -> List[schemas.Category]:
    return db.query(models.Category).filter(models.Category.group_id == group_id).all()


def create_budget(db: Session, budget: schemas.BudgetCreate) -> schemas.Budget:
    db_budget = models.Budget(budgeted=budget.budgeted, activity=budget.activity)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget


def get_budget(db: Session, budget_id: int) -> schemas.Budget:
    return db.query(models.Budget).filter(models.Budget.id == budget_id).first()


def get_group_budgets(db: Session, group_id: int) -> List[schemas.Budget]:
    return db.query(models.Budget).filter(models.Budget.group_id == group_id).all()


def get_category_budgets(db: Session, category_id: int) -> List[schemas.Budget]:
    return db.query(models.Budget).filter(models.Budget.category_id == category_id).all()
