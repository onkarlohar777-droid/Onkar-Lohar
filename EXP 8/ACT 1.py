class InsufficientBalanceError(Exception):
    pass

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance in your account.")
        elif amount <= 0:
            raise ValueError("Enter a valid withdrawal amount.")
        else:
            self.balance -= amount
            print("Withdrawal successful!")
            print(f"Remaining balance: {self.balance}")

# Main program
try:
    initial_balance = float(input("Enter your account balance: "))
    atm = ATM(initial_balance)
    
    amount = float(input("Enter amount to withdraw: "))
    atm.withdraw(amount)

except InsufficientBalanceError as e:
    print("Error:", e)

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

finally:
    print("Thank you for using ATM.")
  
