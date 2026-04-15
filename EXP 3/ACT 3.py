# Code for Emi calculation
principal = float(input("enter principal amount: "))
monthlyintrest = float(input("enter month monthly intrest: "))
year = float(input("enter loan tenure (in years): "))

months = year * 12
monthlyintrest = monthlyintrest / 100
emi = (principal * monthlyintrest * (1 + monthlyintrest)**months) / ((1 + monthlyintrest)**months - 1)

print("your emi is", round(emi, 2))
