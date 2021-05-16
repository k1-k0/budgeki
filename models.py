from sqlalchemy import Column, ForeignKey, Integer, Float, String, DateTime
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
    value = Column(Float)
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
    budgets = relationship('Budget', back_populates='group')


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='categories')
    budgets = relationship('Budget', back_populates='category')
    transactions = relationship('Transaction', back_populates='category')


class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True, index=True)
    budgeted = Column(Float)
    activity = Column(Float)
    timestamp = Column(DateTime)
    category_id = Column(Integer, ForeignKey('categories.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    amount = Column(Float)
    from_category_id = Column(Integer, ForeignKey('categories.id'))
    to_category_id = Column(Integer, ForeignKey('categories.id'))
    from_category = relationship('Category', back_populates='categories')
    to_category = relationship('Category', back_populates='categories')
