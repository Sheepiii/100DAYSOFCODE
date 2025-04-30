print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ").lower()
if size == "s":
   bill += 15
   #print(f"Your bill currently is {bill} ")
elif size == "m":
    bill += 20
    #print(f"Your bill currently is {bill}")
elif size == "l":
   bill += 25
   #print(f"Your bill currently is {bill}")
else:
   print("You typed the wrong input")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
if pepperoni == "y":
   if size == "s":
       bill += 2
   else:
       bill += 3
#print(f"Your current bill is ${bill}")
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
if extra_cheese == "y":
   bill += 1
   #print(f"Your final bill is ${bill}")
#else:
   #print(f"Your final bill is ${bill}!")
print(f"Your final bill is: ${bill}.")

#All of the code greyed out will give the bill as we go through the options
#currently the code achieves the goal of the course