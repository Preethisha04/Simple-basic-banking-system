#creationg a class constructocdr
class Account:
    def __init__(self, name, account_number, balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("\n\t\t\t\t\t\t\tBANKING SYSTEM USING OOP \n")
        print("----------------------------------------------------------------------------------------------------------------------------------")
    def deposit(self,amount):
        self.balance+=amount
        print(f"\n{self.name} Deposited ₹{amount}.\nCurrent balance: ₹{self.balance}\n")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\n{self.name} Withdrew ₹{amount}.\nCurrent balance: ₹{self.balance}\n")
        else:
            print("You don't have enough amount to withdraw from your account.")   
#inheritance 
class Savings_Account(Account): #sub class of Account
    def __init__(self, name, account_number, balance, intrest_rate):
        super().__init__(name, account_number, balance)
        self.interest_rate=intrest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

account1 = Account("John Doe", "123456", 1000)
account1.deposit(500)
account1.withdraw(200)
print()

savings_account = Savings_Account("John Doe", "789012", 2000, 0.05)
savings_account.deposit(1000)
savings_account.add_interest()
savings_account.withdraw(500)
savings_account.withdraw(1000)
    
    