import random

try:
    # Generate 6-digit OTP
    otp = random.randint(100000, 999999)
    print("Your OTP is:", otp)

except Exception as e:
    print("Error:", e)

finally:
    print("OTP generation completed.")
  
