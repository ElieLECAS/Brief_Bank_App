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


# Tests pour les Transferts (Transfer)

class TestTransfers:
    def setup_method(self):
        self.transaction = models.Transaction()

    def test_transfer_normal(self, db_session):
        account1 = models.Account(100, db_session)
        solde_depart1 = account1.balance
        account2 = models.Account(100, db_session)
        solde_depart2 = account2.balance

        transfer = 50
        self.transaction.transfer(expediteur=account1,amount=transfer,destinataire=account2,session=db_session)
        
        assert account1.balance == solde_depart1 - transfer
        assert account2.balance == solde_depart2 + transfer
        # assert self.transaction.type == "Deposite"
        # assert self.transaction.type == "Withdraw"

    def test_transfer_insufficient_funds(self, db_session):
        account1 = models.Account(100, db_session)
        solde_depart1 = account1.balance
        account2 = models.Account(100, db_session)
        solde_depart2 = account2.balance

        transfer = 500
        self.transaction.transfer(expediteur=account1,amount=transfer,destinataire=account2, session=db_session)
        assert account1.balance == solde_depart1
        assert account2.balance == solde_depart2

    def test_transfer_negative_amount(self, db_session):
        account1 = models.Account(100, db_session)
        solde_depart1 = account1.balance
        account2 = models.Account(100, db_session)
        solde_depart2 = account2.balance

        transfer = -50
        self.transaction.transfer(expediteur=account1,amount=transfer,destinataire=account2, session=db_session)
        # assert test == True
        assert account1.balance == solde_depart1
        assert account2.balance == solde_depart2

    def test_transfer_zero_amount(self, db_session):
        account1 = models.Account(100, db_session)
        solde_depart1 = account1.balance
        account2 = models.Account(100, db_session)
        solde_depart2 = account2.balance

        transfer = 0
        self.transaction.transfer(expediteur=account1,amount=transfer,destinataire=account2, session=db_session)
        assert account1.balance == solde_depart1
        assert account2.balance == solde_depart2