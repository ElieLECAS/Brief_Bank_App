import pytest
import tuto.models as models
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='function')
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    db_session = Session()
    models.Base.metadata.create_all(engine)
    yield db_session
    db_session.close()

class TestGetBalance:
    # def setup_method(self):
    #     self.account = models.Account()

    def test_get_balance_initial(self,db_session):
        initial = random.randint(0,1000000)
        account_initial = models.Account(initial,db_session)
        assert account_initial.get_balance() == initial

    def test_get_balance_after_deposit(self, db_session):
        initial = random.randint(100,1000000)
        account = models.Account(initial, db_session)
        self.transaction = models.Transaction()
        solde_depart = account.balance
        depot = 5
        self.transaction.deposit(account=account,amount=depot, session=db_session)
        assert account.get_balance() == solde_depart + depot

    def test_get_balance_after_withdrawal(self, db_session):
        initial = random.randint(100,1000000)
        account = models.Account(initial, db_session)
        self.transaction = models.Transaction()
        solde_depart = account.balance
        retrait = random.randint(1,99)
        self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert account.get_balance() == solde_depart - retrait

    def test_get_balance_after_failed_withdrawal(self, db_session):
        initial = random.randint(10,100)
        account = models.Account(initial, db_session)
        self.transaction = models.Transaction()
        solde_depart = account.balance
        retrait = random.randint(initial+1,initial+100000)
        self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert account.get_balance() == solde_depart
        
    def test_get_balance_after_transfer(self, db_session):
        initial1 = random.randint(10,10000)
        account1 = models.Account(initial1, db_session)
        solde_depart1 = account1.balance

        initial2 = random.randint(10,100)
        account2 = models.Account(initial2, db_session)
        solde_depart2 = account2.balance


        self.transaction = models.Transaction()
        retrait = 100

        self.transaction.transfer(expediteur=account1, amount=retrait, destinataire=account2, session=db_session)
        assert account1.get_balance() == solde_depart1 - retrait
        assert account2.get_balance() == solde_depart2 + retrait