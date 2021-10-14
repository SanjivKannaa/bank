class account():
    def __init__(self, source, account_no, password):
        account.source = source
        account.account_no = account_no
        account.password = password
        account.balance = 0
    def update_balance(self, amount_deducted):
        account.balance -= amount_deducted

while True:
    print("1. Create new account\n2. view balance\n3. update balance")
    choice = input()
    if choice == "1":
        account_1 = account(source = input("bank/company name : "), account_no=input("account number (if any) : "), password=input("password (if any) : "))
    elif choice == "2":
        print("balance = ", account_1.balance)
    elif choice == "3":
        account_1.update_balance(int(input("amount to be reduced : ")))
    else:
        print("wrong input!")