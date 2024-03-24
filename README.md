# "Simple-basic-banking-system"
# > This is my first small step towards learning Object Oriented Programming in python :)
# > source code from freecodecamp (with some little changes i did)
# > so this code is for a basic banking system which comprises of two classes Account and Saving_Account(which is sub class of Account),used the concept of inheritance.
# > Account class has a constructor and other methods(deposit,withdrew)
# > A constructor ( __init__() ) is a special type of method that is automatically called when an object of a class is created,this has been used get the basic information like name,account_number,balance.
# > The deposit method allows users to add funds to their account.
# > The withdraw method allows users to withdraw funds from their account.
# > Saving_Account class has a constructor and other method(add_inetrest)
# > The constructor accepts four parameters: name which is the name of the account holder,  account_number, which is a unique identifier for the savings account, balance, which is the initial balance of the account, and interest_rate, which is the annual interest rate (expressed as a decimal) for the account.
# > The super().__init__(name, account_number, balance) line calls the constructor of the parent class (Account) to initialize the account number and balance.
# > The add_interest method calculates and adds interest to the account balance.
# "I think this short explanation helps you:)"
