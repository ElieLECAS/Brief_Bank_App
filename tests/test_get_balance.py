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

    # Test_get_balance_initial
        # Vérifier le solde initial lorsqu'un nouveau compte est créé.
        # Créer un nouveau compte avec un solde initial spécifique.
        # Utiliser get_balance pour vérifier que le solde retourné correspond au solde initial.
        # Assurer que le résultat est exact sans avoir effectué de transactions.


    def test_get_balance_initial(self,db_session):
        initial = random.randint(0,1000000)
        account_initial = models.Account(initial,db_session)
        assert account_initial.get_balance() == initial
        



    # test_get_balance_after_deposit
        # Vérifier le solde après un dépôt.
        # Effectuer un dépôt sur un compte.
        # Utiliser get_balance pour vérifier que le solde retourné inclut le montant déposé.
        # Vérifier que le solde retourné est égal au solde initial plus le montant du dépôt.

    def test_get_balance_after_deposit(self, db_session):
        initial = random.randint(100,1000000)
        account = models.Account(initial, db_session)
        self.transaction = models.Transaction()
        solde_depart = account.balance
        depot = 5
        self.transaction.deposit(account=account,amount=depot, session=db_session)
        assert account.get_balance() == solde_depart + depot





    # test_get_balance_after_withdrawal
        # Vérifier le solde après un retrait.
        # Effectuer un retrait sur un compte avec un solde suffisant.
        # Utiliser get_balance pour vérifier que le solde retourné a été correctement déduit du montant retiré.
        # Vérifier que le solde retourné est égal au solde initial moins le montant du retrait.

    def test_get_balance_after_withdrawal(self, db_session):
        initial = random.randint(100,1000000)
        account = models.Account(initial, db_session)
        self.transaction = models.Transaction()
        solde_depart = account.balance
        retrait = random.randint(1,99)
        self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert account.get_balance() == solde_depart - retrait



    # test_get_balance_after_failed_withdrawal
        # Vérifier le solde après une tentative de retrait échouée due à un solde insuffisant.
        # Tenter de retirer un montant supérieur au solde disponible.
        # Utiliser get_balance pour vérifier que le solde n'a pas changé
        # Vérifier que le solde retourné est toujours égal au solde initial avant la tentative de retrait.


    def test_get_balance_after_failed_withdrawal(self, db_session):
        initial = random.randint(10,100)
        account = models.Account(initial, db_session)
        self.transaction = models.Transaction()
        solde_depart = account.balance
        retrait = random.randint(initial+1,initial+100000)
        self.transaction.withdraw(account=account,amount=retrait, session=db_session)
        assert account.get_balance() == solde_depart






    # test_get_balance_after_transfer
        # Vérifier le solde après un transfert entre deux comptes.
        # Effectuer un transfert d'un montant spécifique d'un compte à un autre.
        # Utiliser get_balance pour vérifier les soldes des deux comptes après le transfert.
        # Pour le compte source, vérifier que le solde a diminué du montant transféré.
        # Pour le compte cible, vérifier que le solde a augmenté du montant transféré.


        
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