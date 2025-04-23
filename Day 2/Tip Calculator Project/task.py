print("Welcome to the Tip Calculator!")
bill_amount = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15?"))
people_amount = int(input("How many people to split the bill?"))
tip_as_percent = tip_amount / 100
total_tip_amount = bill_amount * tip_as_percent
total_bill_amount = bill_amount + total_tip_amount
amount_to_pay = round((total_bill_amount/people_amount),2)
print(f"Each person will pay: ${amount_to_pay}")




