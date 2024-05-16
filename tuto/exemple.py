from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from models import Base, Account, Transaction

engine = create_engine('sqlite:///bank_bdd.db')
Session = scoped_session(sessionmaker(bind=engine))

try:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    account1 = Account()
    account2 = Account()
    account3 = Account()
    account4 = Account()

    transaction1 = Transaction()
    transaction1.deposit(account1, 34.0, session)

    transaction2 = Transaction()
    transaction2.deposit(account2,100.0, session)

    transaction3 = Transaction()
    transaction3.deposit(account3,150.0, session)

    transaction4 = Transaction()
    transaction4.deposit(account4,222.0, session)

    transaction5 = Transaction()
    transaction5.withdraw(account1,4, session)

    transfer1_2 = Transaction()
    transfer1_2.transfer(account1,9,account2, session)

    account1.get_balance()
    account2.get_balance()

    session.commit()



except Exception as ex:
    print(ex)