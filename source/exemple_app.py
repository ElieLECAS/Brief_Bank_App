from bank import Account
from init_db import Session, Base , engine


def main():
	session = Session()
	account1 = Account(balance=0)
	session.add(account1)
	session.commit()

	# # Emprunt d'un livre
	# account1.borrow("Alice")

	# # Vérification des emprunts
	# transactions = session.query(Transaction).all()
	# for transaction in transactions:
	# 	print(f"{transaction.borrower} has borrowed {transaction.account.title} on {transaction.borrow_date}")

	session.close()
	
if __name__ == "**main**":
	main()