import sys
class Customer():
    bankname='Mahesh Bank'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Balance of after deposit',self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficiant Balance ,You are drawing more then what you have ')
            sys.exit()
        self.balance=self.balance-amount
        print('Balance after withdraw',self.balance)
print("welcome to ",Customer.bankname)
name=input("Enter Your Name:")
c=Customer(name)
while True:
    print('d-Deposit \nw-Withdraw \ne-exit')
    option=input("Choose your option:")
    if option=='d' or option=='D':
        amount=float(input("Enter amount:"))
        c.deposit(amount)
    elif option=='w' or option=='W':
        amount=float(input("Enter amount:"))
        c.withdraw(amount)

    elif option=='e' or option=='E':
        print('Thanks for Banking')
        sys.exit()
    else:
        print("Invalid option choose valid option")
