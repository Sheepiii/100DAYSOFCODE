print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
print("")
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay 5.")
    elif age <= 18:
        print("Please pay 7.")
    elif age <=22:
        print("Please pay 18.")
    else:
        print("You cannot come into weeny hut juniors, unless you pay 100.")
else:
    print("Sorry you have to grow taller before you can ride.")
