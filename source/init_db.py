from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from datetime import datetime

# init_db.py ###
Base = declarative_base()
engine = create_engine('sqlite:///library.db')
Session = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine)
######


# bank.py ####
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

#####

# example_app.py ####
def main():
	session = Session()
	# Ajout de nouveaux livres
	account1 = Account(title="1984", author="George Orwell")
	session.add(account1)
	session.commit()
	
	# Emprunt d'un livre
	account1.borrow("Alice")
	
	# Vérification des emprunts
	transactions = session.query(Transaction).all()
	for transaction in transactions:
	    print(f"{transaction.borrower} has borrowed {transaction.account.title} on {transaction.borrow_date}")
	
	session.close()
	
if __name__ == "**main**":
	main()
	
	#####