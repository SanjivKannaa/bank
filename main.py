import pickle
import time

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

def login():
    print("WELCOME TO BANK!")
    print("\n\n Please LOGIN to continue...")
    account_number = input("account number : ")
    password = input("password : ")
    d = open("account_handler.bin", "rb")
    account_handler = dict(pickle.load(d))
    d.close()
    for i in account_handler.keys():
        if account_handler[i].account_no == account_number:
            return i
    print("\n\nWrong credentials!")
    time.sleep(1)
    login()







f = open("account_handler.bin", "rb")
account_handler = dict(pickle.load(f))
f.close()

# account_logged_in = account(source = input("bank/company name : "), account_no=input("account number (if any) : "), password=input("password (if any) : "), initial_balance=int(input("Enter the initial amount to be put in the account : ")))
account_logged_in = login()


while True:
    print("\t\t\t\t\t welcome ", account_logged_in.account_no)
    print("1. Create new account\n2. view balance\n3. update balance\n4. Online transaction")
    print("99. logout")
    choice = input()
    if choice == "1":
        account_handler[len(account_handler)] = account(source = input("bank/company name : "), account_no=input("account number (if any) : "), password=input("password (if any) : "), initial_balance=int(input("Enter the initial amount to be put in the account : ")))
    elif choice == "2":
        print("balance = ", account_logged_in.balance)
    elif choice == "3":
        account_logged_in.update_balance(input("add/spent?"), int(input("amount : ")))
    elif choice == "4":
        account_logged_in.new_transaction(to_ = input("to account number : "), amount=int(input("Amount to be sent : ")))
    elif choice == "99":
        print("successfully logged out")
        time.sleep(2)
        login()
    elif choice == "exit":
        break
    else:
        print("wrong input!")

f = open("account_handler.bin", "wb")
pickle.dump(account_handler, f)
f.close()

