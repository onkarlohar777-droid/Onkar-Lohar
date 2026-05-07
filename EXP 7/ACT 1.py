class BankAccount:
def _init(self, account_holder, balance-0):
self.account_holder account_holder
self.balance balance
def deposit(self, amount):
if amount > 0:
self.balance+ amount
lprint("Deposited (amount). New balance: r(self.balance)")

else:
print("Invalid deposit amount")
def withdraw(self, amount):
if amount 0:
print("Invalid withdrawal amount")
elif amount self.balance:
print("Insufficient balance")

else:
self.balance amountprint("Withdrawn (amount). Remaining balance: r(self.balance)")
def display_balance(self):
print(f"Account Holder: (self.account_holder)") print(f"Current Balance: r(self.balance)")
