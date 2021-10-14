import time
import pickle

class account():
    def __init__(self, source, account_no, password, initial_balance):
        account.source = source
        account.account_no = account_no
        account.password = password
        account.balance = initial_balance
    def update_balance(self, update_type, amount):
        if update_type == "add":
            account.balance += amount
        elif update_type in ["deduct", "spent"]:
            account.balance -= amount
    def new_transaction(self, to_, amount):
        if make_new_transaction(from_ = account.account_no, to_ = to_, amount = amount):
            account.balance -= amount
    

def make_new_transaction(from_, to_, amount):
    return True


f = account(source = input("bank/company name : "), account_no=input("account number (if any) : "), password=input("password (if any) : "), initial_balance=int(input("Enter the initial amount to be put in the account : ")))
d = {
    0 : f
}

print(d[0].account_no)