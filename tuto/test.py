from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship

engine = create_engine('sqlite:///bank_bdd.db')
Session = scoped_session(sessionmaker(bind=engine))

try:
    conn = engine.connect()
    print('Success!')
except Exception as ex:
    print(ex)