class Bankaccount():
    def __init__(self,holdername,balance):
        self.holdername=holdername
        self.balance=balance
    def display(self):
        print(self.holdername,self.balance)
bnk=Bankaccount("Krishnaprasad",150000)
bnk.display()
