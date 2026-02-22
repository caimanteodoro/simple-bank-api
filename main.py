# main.py

from user import User
from account import Account

users = []
accounts = []

def find_account(account_id):
    for acc in accounts:
        if acc.account_id == account_id:
            return acc
    return None

def main():
    while True:
        print("\n=== SIMPLE BANK ===")
        print("1 - Criar usuário")
        print("2 - Criar conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Ver saldo")
        print("6 - Ver histórico")
        print("0 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            user_id = input("ID do usuário: ")
            name = input("Nome: ")
            users.append(User(user_id, name))
            print(f"Usuário {name} criado com sucesso!")

        elif choice == "2":
            account_id = input("ID da conta: ")
            user_id = input("ID do usuário dono da conta: ")
            user = next((u for u in users if u.user_id == user_id), None)
            if user:
                accounts.append(Account(account_id, user))
                print(f"Conta {account_id} criada para {user.name}!")
            else:
                print("Usuário não encontrado.")

        elif choice == "3":
            account_id = input("ID da conta: ")
            acc = find_account(account_id)
            if acc:
                amount = float(input("Valor do depósito: "))
                acc.deposit(amount)
            else:
                print("Conta não encontrada.")

        elif choice == "4":
            account_id = input("ID da conta: ")
            acc = find_account(account_id)
            if acc:
                amount = float(input("Valor do saque: "))
                acc.withdraw(amount)
            else:
                print("Conta não encontrada.")

        elif choice == "5":
            account_id = input("ID da conta: ")
            acc = find_account(account_id)
            if acc:
                acc.show_balance()
            else:
                print("Conta não encontrada.")

        elif choice == "6":
            account_id = input("ID da conta: ")
            acc = find_account(account_id)
            if acc:
                acc.show_transactions()
            else:
                print("Conta não encontrada.")

        elif choice == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
