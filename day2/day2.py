# 100 Days of Code: Day 2

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?"))
tip_percent = int(input("What percentage tip what you like to give? 10, 12 or 15?"))/100
ppl = int(input("How many people to split the bill?"))
spend_per_person = round((bill + tip_percent*bill)/ppl,2)
print(f"Each person should pay {spend_per_person}")


