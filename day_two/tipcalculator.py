# Day 2 of 100 - Tip Calculator

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_amount = float(input("How many people split the bill? "))
amount_per_person = round((total_bill / split_amount) * (1 + (tip_percentage / 100)),2)

print(f"Each person should pay: ${amount_per_person}")
