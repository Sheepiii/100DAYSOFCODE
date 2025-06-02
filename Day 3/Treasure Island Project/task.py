print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction = input("\tType: 'Left' or 'Right'\n").lower()
wait = ""
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait = input("\tType 'wait' to wait for a boat. Type 'Swim' to swim across\n").lower()
elif direction == "right":
    print("You fell into a hole. GAME OVER!")
else:
    print("wrong input -1 life")

if wait == "swim":
    print("\tAttacked by Angry trout\n \t    Game Over!")
elif wait == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors.")
    door_color = input("\tOne red,one yellow and one blue. Which colour do you choose?\n").lower()
    if door_color == "red":
        print("Burned by the Fire Lord!\n \tGAME OVER!")
    elif door_color == "blue":
        print("Eaten by the Hydra!\n \tGAME OVER!")
    elif door_color == "yellow":
        print("\tYOU WIN!")
    else:
        print("Choose a color!\n Also..YOU DIED!")
else:
    print("YOU DIED!")

#treasure island complete woioioo