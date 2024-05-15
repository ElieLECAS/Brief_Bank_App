import pytest
import tuto.models as models



# Tests pour les Dépots (Deposit)

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

    def test_deposit_normal(self):
        account = models.Account(10)
        solde_depart = account.balance
        depot = 5
        test = self.transaction.deposit(account=account,amount=depot)
        assert test == True
        assert account.balance == solde_depart + depot
        assert self.transaction.type == "Deposit"

    # Test_deposit_negative_amount

        # 1.Tenter de déposer un montant négatif.
        # 2.Vérifier que le solde du compte n'a pas changé.
        
        # À faire
            # 3.Vérifier qu'aucune transaction n'est créée.
            # 4.Vérifier que le session.commit() a été appelé.

    def test_deposit_negative_amount(self):
        account = models.Account(10)
        solde_depart = account.balance
        depot = -5
        test = self.transaction.deposit(account=account,amount=depot)
        assert test == False
        assert account.balance == solde_depart
        assert self.transaction.type == "Deposit"

    # Test_deposit_zero_amount

        # 1.Tenter de déposer un montant négatif.
        # 2.Vérifier que le solde du compte n'a pas changé.
        
        # À faire
            # 3.Vérifier qu'aucune transaction n'est créée.
            # 4.Vérifier que le session.commit() a été appelé.
    

    def test_deposit_zero_amount(self):
        account = models.Account(10)
        solde_depart = account.balance
        depot = 0
        test = self.transaction.deposit(account=account,amount=depot)
        assert test == False
        assert account.balance == solde_depart
        assert self.transaction.type == "Deposit"

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

    def test_withdraw_normal(self):
        account = models.Account(10)
        solde_depart = account.balance
        retrait = 5
        test = self.transaction.withdraw(account=account,amount=retrait)
        assert test == True
        assert account.balance == solde_depart - retrait
        assert self.transaction.type == "Withdraw"

    #  Test_withdraw_insufficient_funds

        # 1.Tenter de retirer un montant supérieur au solde disponible.
        # 2.Vérifier que le solde reste inchangé.

        # À faire
            # 3.Vérifier qu'aucune transaction n'est ajoutée.
            # 4.Vérifier que le session.commit() n'a pas été ajouté.

    def test_withdraw_insufficient_funds(self):
        account = models.Account(10)
        solde_depart = account.balance
        retrait = 15
        test = self.transaction.withdraw(account=account,amount=retrait)
        assert test == False
        assert account.balance == solde_depart

    # Test_withdraw_negative_amount

        # 1.Tenter de retirer un montant négatif.
        # 2.Vérifier que le solde reste inchangé.

        # À faire
            # 3.Vérifier qu'aucune transaction n'est créée.
            # 4.Vérifier que le session.commit() n'a pas été ajouté.

    def test_withdraw_negative_amount(self):
        account = models.Account(10)
        solde_depart = account.balance
        retrait = -15
        test = self.transaction.withdraw(account=account,amount=retrait)
        assert test == False
        assert account.balance == solde_depart


    # Test_withdraw_zero_amount

        # 1.Tenter de retirer un montant nul..
        # 2.Vérifier que le solde reste inchangé.

        # À faire
            # 3.Vérifier qu'aucune transaction n'est créée.
            # 4.Vérifier que le session.commit() n'a pas été ajouté.

    def test_withdraw_zero_amount(self):
        account = models.Account(10)
        solde_depart = account.balance
        retrait = 0
        test = self.transaction.withdraw(account=account,amount=retrait)
        assert test == False
        assert account.balance == solde_depart
    


# Tests pour les Transferts (Transfer)

class TestTransfers:
    def setup_method(self):
        self.transaction = models.Transaction()

    # Test_transfer_normal
        # Effectuer un transfert entre deux comptes avec des soldes suffisants.
        # Vérifier que le montant est déduit du compte source.
        # Vérifier que le montant est ajouté au compte cible.
        # Vérifier que deux transactions sont créées avec les types appropriés.
        # Vérifier que le session.commit() n'a pas été ajouté.

    def test_transfer_normal(self):
        account1 = models.Account(100)
        solde_depart1 = account1.balance
        account2 = models.Account(100)
        solde_depart2 = account2.balance

        transfer = 50
        self.transaction.transfer(expediteur=account1,amount=transfer,destinataire=account2)
        # assert test == True
        assert account1.balance == solde_depart1 - transfer
        assert account2.balance == solde_depart2 + transfer

