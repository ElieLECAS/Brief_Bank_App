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

    account1.withdraw(33)

    transaction1 = Transaction()
    transaction2 = Transaction()
    transaction3 = Transaction()
    transaction4 = Transaction()

    transaction1.deposit(account1, 34.0)
    transaction2.deposit(account2,100.0)
    transaction3.deposit(account3,150.0)
    transaction4.deposit(account4,222.0)

    session.add(account1)
    session.add(account2)
    session.add(account3)
    session.add(account4)

    session.add(transaction1)
    session.add(transaction2)
    session.add(transaction3)
    session.add(transaction4)

    session.commit()


except Exception as ex:
    print(ex)