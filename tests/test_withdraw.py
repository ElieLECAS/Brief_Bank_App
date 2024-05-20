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

# Tests pour les Retraits (Withdraw)

class TestWithdraw:
    def setup_method(self):
        self.transaction = models.Transaction()

    def test_withdraw_normal(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        retrait = 5
        test = self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert test == True
        assert account.balance == solde_depart - retrait
        assert self.transaction.type == "Withdraw"

    def test_withdraw_insufficient_funds(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        retrait = 15
        test = self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert test == False
        assert account.balance == solde_depart

    def test_withdraw_negative_amount(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        retrait = -15
        test = self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert test == False
        assert account.balance == solde_depart

    def test_withdraw_zero_amount(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        retrait = 0
        test = self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert test == False
        assert account.balance == solde_depart
    


