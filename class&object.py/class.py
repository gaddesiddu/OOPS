class Bank:
    def __init__(self,accountNo,accountName,ifscNo,balance):
        self.accountNo=accountNo
        self.accountName=accountName
        self.ifscNo=ifscNo
        self.balance=balance
    def withdraw(self,amount):
        self.balance-= amount
    def deposit(self,amount):
        self.balance+=amount
    def checkbalance(self):
        print(self.balance)

o1=Bank(1,"siddu","SBINOO",50000)
o1.withdraw(1000)
o1.checkbalance()