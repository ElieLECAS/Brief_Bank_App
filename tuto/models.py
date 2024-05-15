from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, ForeignKey, Float, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from datetime import datetime

Base = declarative_base()

engine = create_engine('sqlite:///bank_bdd.db')
Session = scoped_session(sessionmaker(bind=engine))
Session = sessionmaker(bind=engine)
session = Session()

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    balance = Column(Float)
    transactions = relationship("Transaction", back_populates="account")  # Relation avec les emprunts

    def __init__(self):
        self.balance = 0.0
        session.add(self)
        session.commit()

    def get_balance(self):
        print(self.balance)

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    amount = Column(Float)
    type = Column(String)
    published_date = Column(DateTime, default=datetime.now)
    account = relationship("Account", back_populates="transactions")

    
    def deposit(self, account, amount):
        self.account_id = account.id
        self.amount = amount
        self.type = 'Deposit'
        account.balance += amount
        session.add(self)
        session.commit()
        return True
    
    def withdraw(self, account, amount):
        self.account_id = account.id
        self.amount = amount
        self.type = 'Withdraw'
        account.balance -= amount
        session.add(self)
        session.commit()
        return True

    def transfer(self, expediteur, amount, destinataire):
        retrait = Transaction()
        retrait.withdraw(expediteur, amount)
        depot = Transaction()
        depot.deposit(destinataire, amount)
        return 