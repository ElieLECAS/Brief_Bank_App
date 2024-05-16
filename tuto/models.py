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

    def __init__(self, balance=0):
        self.balance = balance
        session.add(self)
        # session.commit()

    def get_balance(self):
        print(self.balance)
        return self.balance

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
        if amount > 0:
            account.balance += amount
            session.add(self)
            # session.commit()
            print(f'Dépot de {amount}€ effectué')
            return True
        else:
            print(f'Dépot de {amount}€ annulé')
            return False

    
    def withdraw(self, account, amount):
        self.account_id = account.id
        self.amount = amount
        self.type = 'Withdraw'
        if amount > 0 and account.balance >= amount:
            account.balance -= amount
            session.add(self)
            # session.commit()
            print(f'Retrait de {amount}€ validé')
            return True
        else:
            print(f'Retrait de {amount}€ annulé')
            return False


    def transfer(self, expediteur, amount, destinataire):
        retrait = Transaction()
        depot = Transaction()

        if retrait.withdraw(expediteur, amount):
            depot.deposit(destinataire, amount)
            print(f'Transfert de {amount}€ effectué')
        else:
            print(f'Transfert de {amount}€ annulé')
        return 