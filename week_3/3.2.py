class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance if balance >= 0 else 0

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def check_balance(self):
        return self.balance


alice = BankAccount("Alice", 500)
print(alice.check_balance())
alice.deposit(200)
print(alice.check_balance())
alice.withdraw(100)
print(alice.check_balance())