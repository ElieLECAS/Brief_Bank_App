from bank import Account
from init_db import Session, Base, engine
from datetime import datetime

def main():
    session = Session()

    account1 = Account(balance=0)
    session.add(account1)
    session.commit()

    account1.create_account()

    account1.deposit(100)

    account1.withdraw(50)

    account2 = Account(balance=0)
    session.add(account2)
    session.commit()

    account2.create_account()

    amount_to_transfer = 50
    account1.transfer(amount_to_transfer, account2)

    # Affichage des soldes des comptes après les opérations
    print("Solde du compte 1:", account1.get_balance())
    print("Solde du compte 2:", account2.get_balance())

    session.close()

if __name__ == "main":
    main()
