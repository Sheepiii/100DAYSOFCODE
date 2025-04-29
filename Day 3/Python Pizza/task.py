print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ").lower()
if size == "s":
    bill = 15
    print(f"Your bill currently is {bill} ")
elif size == "m":
        bill = 20
        print(f"Your bill currently is {bill}")
elif size == "l":
        bill = 25
        print(f"Your bill currently is {bill}")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

extra_cheese = input("Do you want extra cheese? Y or N: ")

