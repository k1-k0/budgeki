from sqlalchemy import Column, ForeignKey, Integer, Float, String, Time
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    accounts = relationship('Account', back_populates='owner')


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='accounts')
    groups = relationship('Group', back_populates='account')


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', back_populates='groups')
    categories = relationship('Category', back_populates='group')


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='categories')
    budget = relationship('Budget', back_populates='category')


class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    budgeted = Column(Float)
    activity = Column(Float)
    timestamp = Column(Time)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='categories')
