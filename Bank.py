class SavingsAccount:
    def __init__(self, name_of_account_holder, initial_balance, pin_number):
        self.name_of_account_holder = name_of_account_holder
        self.initial_balance = initial_balance
        self.pin_number = pin_number
    def display_details(self):
        print("saving account details")
        print(f"name of account holder: {self.name_of_account_holder}")
        print(f"initial balance: ₹{self.initial_balance}")
        print(f"pin number: {self.pin_number}")
savings_acc = SavingsAccount("Jaya Sri", 10000, 1234)
savings_acc.display_details()


class SavingsAccount:
    def _init_(self, holder_name, initial_balance, pin):
        self.holder_name = holder_name
        self.balance = initial_balance
        self.pin = pin
        self.is_active = True  
    def check_balance(self, entered_pin):
        if not self.is_active:
            return "Account inactive"
        elif entered_pin != self.pin:
            return "Incorrect PIN"
        else:
            return f"Current Balance:{self.balance}"

account = SavingsAccount("Jayasri", 5000, 1234)
print("Test 1:", account.check_balance(1234))
print("Test 2:", account.check_balance(9999))  
account.is_active = False
print("Test 3:", account.check_balance(1234))  

class SavingsAccount:
    def _init_(self, name, balance, pin, daily_limit=50000):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.active = True
        self.daily_limit = daily_limit
    def withdraw(self, entered_pin, amount):
        print(f"\n Withdraw Funds")
        if entered_pin != self.pin:
            print("Error: Incorrect PIN.")
            return
        if not self.active:
            print("Error: Account inactive. Withdrawal not allowed.")
            return
        if amount > self.balance:
            print("Error: Insufficient balance.")
            return
        if amount > self.daily_limit:
            print("Error: Amount exceeds daily withdrawal limit.")
            return
        self.balance -= amount
        print(f"Withdrawal successful! ₹{amount} deducted.")
        print(f"Remaining Balance: ₹{self.balance}")
   


