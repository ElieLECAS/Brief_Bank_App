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

    # Test_transfer_normal

        # Effectuer un transfert entre deux comptes avec des soldes suffisants.
        # Vérifier que le montant est déduit du compte source.
        # Vérifier que le montant est ajouté au compte cible.

        # À faire
            # Vérifier que deux transactions sont créées avec les types appropriés.
            # Vérifier que le session.commit() n'a pas été ajouté.

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




    # Test_transfer_insufficient_funds

        # Tenter un transfert avec un solde insuffisant sur le compte source.
        # Vérifier que le solde des deux comptes reste inchangé.

        # À faire
            # Vérifier qu'aucune transaction n'est ajoutée pour les deux comptes.
            # Vérifier que le session.commit() n'a pas été ajouté.


    def test_transfer_insufficient_funds(self, db_session):
        account1 = models.Account(100, db_session)
        solde_depart1 = account1.balance
        account2 = models.Account(100, db_session)
        solde_depart2 = account2.balance

        transfer = 500
        self.transaction.transfer(expediteur=account1,amount=transfer,destinataire=account2, session=db_session)
        # assert test == True
        assert account1.balance == solde_depart1
        assert account2.balance == solde_depart2




    # Test_transfer_negative_amount

        # Tenter de transférer un montant négatif.
        # Vérifier que le solde des deux comptes reste inchangé.
        
        # À faire
            # Vérifier qu'aucune transaction n'est ajoutée pour les deux comptes.
            # Vérifier que le session.commit() n'a pas été ajouté.

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

    # Test_transfer_zero_amount

        # Tenter de transférer un montant nul.
        # Vérifier que le solde des deux comptes reste inchangé.

        # À faire
            # Vérifier qu'aucune transaction n'est ajoutée pour les deux comptes.
            # Vérifier que le session.commit() n'a pas été ajouté.

    def test_transfer_zero_amount(self, db_session):
        account1 = models.Account(100, db_session)
        solde_depart1 = account1.balance
        account2 = models.Account(100, db_session)
        solde_depart2 = account2.balance

        transfer = 0
        self.transaction.transfer(expediteur=account1,amount=transfer,destinataire=account2, session=db_session)
        # assert test == True
        assert account1.balance == solde_depart1
        assert account2.balance == solde_depart2