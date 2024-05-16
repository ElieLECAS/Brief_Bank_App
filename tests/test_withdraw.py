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

    # Test_withdraw_normal 

        # 1.Effectuer un retrait avec un solde suffisant.
        # 2.Vérifier que le solde est correctement déduit.
        # 3.Vérifier que la transaction est correctement ajoutée avec le type "withdraw".
        
        # À faire
            # 4.Vérifier que le session.commit() n'a pas été ajouté.

    def test_withdraw_normal(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        retrait = 5
        test = self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert test == True
        assert account.balance == solde_depart - retrait
        assert self.transaction.type == "Withdraw"

    #  Test_withdraw_insufficient_funds

        # 1.Tenter de retirer un montant supérieur au solde disponible.
        # 2.Vérifier que le solde reste inchangé.

        # À faire
            # 3.Vérifier qu'aucune transaction n'est ajoutée.
            # 4.Vérifier que le session.commit() n'a pas été ajouté.

    def test_withdraw_insufficient_funds(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        retrait = 15
        test = self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert test == False
        assert account.balance == solde_depart

    # Test_withdraw_negative_amount

        # 1.Tenter de retirer un montant négatif.
        # 2.Vérifier que le solde reste inchangé.

        # À faire
            # 3.Vérifier qu'aucune transaction n'est créée.
            # 4.Vérifier que le session.commit() n'a pas été ajouté.

    def test_withdraw_negative_amount(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        retrait = -15
        test = self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert test == False
        assert account.balance == solde_depart


    # Test_withdraw_zero_amount

        # 1.Tenter de retirer un montant nul..
        # 2.Vérifier que le solde reste inchangé.

        # À faire
            # 3.Vérifier qu'aucune transaction n'est créée.
            # 4.Vérifier que le session.commit() n'a pas été ajouté.

    def test_withdraw_zero_amount(self, db_session):
        account = models.Account(10, db_session)
        solde_depart = account.balance
        retrait = 0
        test = self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert test == False
        assert account.balance == solde_depart
    


