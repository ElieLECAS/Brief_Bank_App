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

    account1 = Account(0.0)
    account2 = Account(50.0)
    account3 = Account(450.0)
    account4 = Account(20.0)

    session.add(account1)
    session.add(account2)
    session.add(account3)
    session.add(account4)

    session.commit()


except Exception as ex:
    print(ex)