class InvalidAgeError(Exception):
    pass

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    if age <= 0 or age > 120:
        raise InvalidAgeError("Age must be between 1 and 120.")
        
    print("Registration successful!")
    print("Name:", name)
    print("Age:", age)

except ValueError:
    print("Error: Please enter a valid number for age.")

except InvalidAgeError as e:
    print("Error:", e)

finally:
    print("Form submission process completed.")
  
