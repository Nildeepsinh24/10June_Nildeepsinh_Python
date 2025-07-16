class Account:
    def open_account(self):
        self.ac_num = input("Enter Account Number: ")
        self.ac_name = input("Enter Account Holder Name: ")
        self.ac_type = input("Enter Account Type (Savings/Current): ")
        self.balance = 0
        print("Account Opened Successfully.\n")


class Deposit(Account):
    def deposit_amount(self):
        amount = int(input("Enter Deposit Amount: "))
        if amount < 2000:
            print("Amount must be at least Rs.2000.")
            exit()
        else:
            self.balance += amount
            print(f"Rs.{amount} Deposited Successfully.\n")


class Withdraw(Deposit):
    def withdraw_amount(self):
        user_input=input("Do you want To withdraw: Yes Or No:\n")
        if(user_input == "yes"):
            amount = int(input("Enter Withdrawal Amount: "))

            if amount > self.balance:
                print("Insufficient Balance.")
            else:
                self.balance -= amount
                print(f"Rs.{amount} Withdrawn Successfully.\n")

    def show_details(self):
        print("----- ACCOUNT DETAILS -----")
        print("Account Number :", self.ac_num)
        print("Holder Name    :", self.ac_name)
        print("Account Type   :", self.ac_type)
        print("Balance        : Rs.", self.balance)
        print("---------------------------")

acc = Withdraw()

acc.open_account()
acc.deposit_amount()
acc.withdraw_amount()
acc.show_details()