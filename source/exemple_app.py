from init_db import Session
from bank import Account

def main():
	session = Session()
	# Ajout de nouveaux livres
	account1 = Account()
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