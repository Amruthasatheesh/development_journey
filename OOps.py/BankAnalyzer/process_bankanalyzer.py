from csv import DictReader

class TransactionAnalyzer:
    def __init__(self):
        fr=open("OOps.py\\BankAnalyzer\\bank_transactions_500_records.csv","r")
        self.transaction=list(DictReader(fr))
        print(len(self.transaction))

    def debit_transactions(self):
        for t in self.transaction:
            if t.get("type")=="debit":
                print(t)
    def credit_transactions(self):
        for t in self.transaction:
            if t.get("type")=="credit":
                print(t)
    def high_value(self):
        highvalue=[t for t in self.transaction if int(t["amount"])>70000]
        print(highvalue)
    def high_debit(self):
        high = max(int(t["amount"]) for t in self.transaction if t["type"] == "debit")
        print(high)                             

    def high_credit(self):
        high_credit=max(int(t["amount"]) for t in self.transaction if t["type"]=="credit")
        print(high_credit)

analysis_instance=TransactionAnalyzer()
analysis_instance.debit_transactions()
analysis_instance.credit_transactions()
analysis_instance.high_value()
analysis_instance.high_debit()
analysis_instance.high_credit()
#find:
#credit transaction
#high debit transaction,,high value trnsaction>75000,high credit transaction