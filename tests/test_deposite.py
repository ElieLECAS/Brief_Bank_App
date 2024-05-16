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

    # Test_deposit_normal

        # 1.Effectuer un dépôt avec un montant positif..
        # 2.Vérifier que le solde du compte est correctement mis à jour.
        # 3.Vérifier que la transaction est correctement ajoutée avec le type "deposit"
        
        # À faire
            # 4.Vérifier que le timestamp de la transaction est correctement enregistré.
            # 5.Vérifier que le session.commit() a été appelé.

    def test_deposit_normal(self, db_session):
        account = models.Account(10)
        solde_depart = account.balance
        depot = 5
        test = self.transaction.deposit(account=account,amount=depot, session = db_session)
        assert test == True
        assert account.balance == solde_depart + depot
        assert self.transaction.type == "Deposit"

    # Test_deposit_negative_amount

        # 1.Tenter de déposer un montant négatif.
        # 2.Vérifier que le solde du compte n'a pas changé.
        
        # À faire
            # 3.Vérifier qu'aucune transaction n'est créée.
            # 4.Vérifier que le session.commit() a été appelé.

    def test_deposit_negative_amount(self, db_session):
        account = models.Account(10)
        solde_depart = account.balance
        depot = -5
        test = self.transaction.deposit(account=account,amount=depot, session = db_session)
        assert test == False
        assert account.balance == solde_depart
        assert self.transaction.type == "Deposit"

    # Test_deposit_zero_amount

        # 1.Tenter de déposer un montant négatif.
        # 2.Vérifier que le solde du compte n'a pas changé.
        
        # À faire
        #     3.Vérifier qu'aucune transaction n'est créée.
        #     4.Vérifier que le session.commit() a été appelé.
    

    def test_deposit_zero_amount(self, db_session):
        account = models.Account(10)
        solde_depart = account.balance
        depot = 0
        test = self.transaction.deposit(account=account,amount=depot, session = db_session)
        assert test == False
        assert account.balance == solde_depart
        assert self.transaction.type == "Deposit"