class Bank_Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

david_account = Bank_Account()
print(f'Balance: {david_account.balance}')
david_account.deposit(100)
david_account.withdraw(50)
print(f'Balance: {david_account.balance}')
    
