from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from datetime import datetime

from source.init_db import Base, Session


class Account(Base):
	__tablename__ = 'accounts'
	id = Column(Integer, primary_key=True)
	title = Column(String)
	author = Column(String)
	published_date = Column(DateTime, default=datetime.now)
	loans = relationship("Transaction", back_populates="account")  # Relation avec les emprunts


	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __repr__(self):
		return f"<Account(title='{self.title}', author='{self.author}')>"

	def borrow(self, borrower):
		new_transaction = Transaction(account=self, borrower=borrower, borrow_date=datetime.now())
		session = Session()
		session.add(new_transaction)
		session.commit()



class Transaction(Base):
	__tablename__ = 'transactions'
	id = Column(Integer, primary_key=True)
	account_id = Column(Integer, ForeignKey('[account.id](http://account.id/)'))
	borrower = Column(String)
	borrow_date = Column(DateTime)
	account = relationship("Account", back_populates="transactions")