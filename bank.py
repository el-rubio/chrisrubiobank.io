class Account:              #Abstract Parent Class 
    def __init__(self, name, balance, min_balance):    #Constructor (general account class)
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,amount):   #making a deposit
        self.balance += amount

    def withdraw(self, amount): #withdrawing money 
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:               # When funds are NOT available
            print("Sorry, not enough funds!")

    def statement(self):       # print account balance
        print("Account Balance: ${}".format(self.balance))

class Current(Account):
    def __init__(self,name,balance):    #constructor (Parameters to create current account)
        super().__init__(name, balance, min_balance = - 1000)

    def __str__(self):  #define string function 
        return "{}'s Current Account : Balance ${}".format(self.name, self.balance)
    
class Savings(Account):     #Create a class, and inherit
    def __init__(self,name,balance):     #define constructor
        super().__init__(name, balance, min_balance = 0)   # call constructor

    def __str__(self):      #define string function 
        return "{}'s Savings Account : Balance ${}".format(self.name, self.balance)
