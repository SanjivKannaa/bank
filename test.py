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


f = open("account_handler.bin", "rb")
d = dict(pickle.load(f))
f.close()
print(d)
for i in d.keys():
    print(d[i], d[i].account_no)




exit()

f = account(source = "bank", account_no='12345', password="password", initial_balance=100)
f2 = account(source = "bank", account_no='12344', password="password", initial_balance=100)
d = {
    0 : f,
    1 : f2
}

for i in d.keys():
    print(d[i], d[i].account_no)