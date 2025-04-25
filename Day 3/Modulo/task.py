print("Welcome to the Odd or Even Check!")
random_number = int(input("What number are you thinking of?"))
modulo = random_number % 2
if modulo == 0:
    print("You thought of a even number")
else:
    print("You thought of a odd number")