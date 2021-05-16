from typing import List
from datetime import datetime

from pydantic import BaseModel, EmailStr


class TransactionBase(BaseModel):
    amount: float
    from_category: int
    to_category: int


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    timestamp: datetime

    class Config:
        orm_mode = True


class BudgetBase(BaseModel):
    name: str
    budgeted: float = 0
    activity: float = 0


class BudgetCreate(BudgetBase):
    pass


class Budget(BudgetBase):
    id: int
    category_id: int
    timestamp: datetime

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    group_id: int
    budgets: List[Budget]
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True


class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    account_id: int
    categories: List[Category]

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    name: str


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    owner_id: int
    groups: List[Group] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    accounts: List[Account] = []

    class Config:
        orm_mode = True
