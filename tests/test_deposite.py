import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tuto.models as models

@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
    models.Base.metadata.create_all(engine)
    yield session
    session.close()

class TestDeposit:
    def setup_method(self):
        self.transaction = models.Transaction()

    def test_deposit_normal(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        depot = 5
        test = self.transaction.deposit(account=account,amount=depot, session = db_session)
        assert test == True
        assert account.balance == solde_depart + depot
        assert self.transaction.type == "Deposit"

    def test_deposit_negative_amount(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        depot = -5
        test = self.transaction.deposit(account=account,amount=depot, session = db_session)
        assert test == False
        assert account.balance == solde_depart
        assert self.transaction.type == "Deposit"

    def test_deposit_zero_amount(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        depot = 0
        test = self.transaction.deposit(account=account,amount=depot, session = db_session)
        assert test == False
        assert account.balance == solde_depart
        assert self.transaction.type == "Deposit"