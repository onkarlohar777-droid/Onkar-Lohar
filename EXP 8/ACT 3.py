try:
    total_bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))
    
    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    
    share = total_bill / people
    print("Each person should pay:", share)

except ZeroDivisionError:
    print("Error: Cannot divide by zero people.")

except ValueError as e:
    print("Error:", e)

finally:
    print("Bill splitting process completed.")
  
