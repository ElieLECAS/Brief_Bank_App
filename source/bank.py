from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, ForeignKey, Float, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from datetime import datetime

from init_db import Base, Session, engine




class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    balance = Column(Float)
    # transactions = relationship("Transaction", back_populates="account")  # Relation avec les emprunts

    def __init__(self):
        self.balance = 0
        # session = Session()
        # session.add()
        # session.commit()

	# def __repr__(self):
	# 	return f"<Account(title='{self.title}', author='{self.author}')>"

	# def borrow(self, borrower):
	# 	new_transaction = Transaction(account=self, borrower=borrower, borrow_date=datetime.now())
	# 	session = Session()
	# 	session.add(new_transaction)
	# 	session.commit()



class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    amount = Column(Float)
    type = Column(String)
    timestamp = Column(String)

	# account_id = Column(Integer, ForeignKey('[account.id](http://account.id/)'))
	# borrower = Column(String)
	# borrow_date = Column(DateTime)
	# account = relationship("Account", back_populates="transactions")
    
Base.metadata.create_all(engine)