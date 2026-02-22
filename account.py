# account.py

from transaction import Transaction

class Account:
    def __init__(self, account_id, user):
        self.account_id = account_id
        self.user = user
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Valor inválido para depósito.")
            return
        self.balance += amount
        self.transactions.append(Transaction("DEPOSIT", amount))
        print(f"Depósito de R${amount} realizado com sucesso!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Valor inválido para saque.")
            return
        if amount > self.balance:
            print("Saldo insuficiente.")
            return
        self.balance -= amount
        self.transactions.append(Transaction("WITHDRAW", amount))
        print(f"Saque de R${amount} realizado com sucesso!")

    def show_balance(self):
        print(f"Saldo atual: R${self.balance}")

    def show_transactions(self):
        print("Histórico de transações:")
        for t in self.transactions:
            print(f"{t.type} - R${t.amount}")
