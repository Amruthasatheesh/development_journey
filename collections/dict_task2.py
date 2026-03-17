#Create a dictionary:
# account_number
# holder_name
# balance
# Tasks:
# Deposit 5000
# Withdraw 2000
# Check if balance is less than 1000 → print "Low Balance"

bank_details={"account_number":201,"holder_name":"Das","balance":5000}
bank_details["balance"]+=5000

if bank_details["balance"]>2000:

    bank_details["balance"]-=2000
else:
    print("insufficient balance")
if bank_details["balance"] <1000:
    print("low balance")

print(bank_details)


