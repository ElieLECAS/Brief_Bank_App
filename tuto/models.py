from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, ForeignKey, Float, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    balance = Column(Float)
    transactions = relationship("Transaction", back_populates="account")  # Relation avec les emprunts

    def __init__(self, balance):
        self.balance = balance

    def create_account(self):
        pass

    def deposit(self, depos):
        self.balance += depos
        return

    def withdraw(self, retrait):
        self.balance -= retrait
        return

    def transfer(self):
        pass

    def get_balance(self):
        return self.balance

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    amount = Column(Float)
    type = Column(String)
    timestamp = Column(String)
    account = relationship("Account", back_populates="transactions")