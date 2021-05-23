from sqlalchemy import Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    accounts = relationship('Account', back_populates='user')
    groups = relationship('Group', back_populates='user')


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='accounts')


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='groups')
    categories = relationship('Category', back_populates='group')
    budgets = relationship('Budget', back_populates='group')


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='categories')
    budgets = relationship('Budget', back_populates='category')


class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True, index=True)
    budgeted = Column(Float)
    activity = Column(Float)
    timestamp = Column(DateTime)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='budgets')
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='budgets')
    transactions = relationship('Transaction', back_populates='budget')


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    amount = Column(Float)
    budget_id = Column(Integer, ForeignKey('budgets.id'))
    budget = relationship('Budget', back_populates='transactions')
