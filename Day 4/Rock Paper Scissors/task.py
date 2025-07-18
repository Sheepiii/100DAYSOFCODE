import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]#list goes 0,1,2 like the choices for the game

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))#make this a int( to make it a int vs a string response
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])#this will print the image corresponding the list of images


computer_choice = random.randint(0, 2)# Using random,randint will give a number between the listed number

print("Computer chose:")
print(game_images[computer_choice])# will print image corresponding to computer choice

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")#why choose something not listed

elif user_choice == 0 and computer_choice == 2:#rock v scissor
    print("You win!")
elif computer_choice == 0 and user_choice == 2:#rock v scissor
    print("You lose!")
elif computer_choice > user_choice: #scissor v paper
    print("You lose!")
elif user_choice > computer_choice: #scissor v paper
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")