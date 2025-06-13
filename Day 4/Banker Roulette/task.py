import random
#if you are going to use the random module IMPORT it first
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

paying_person = random.choice(friends)
#to make it random you have to make a new variable with the list using the random.choice

print(paying_person)


#2nd option

random_index = random.randint(0,4)
#using an index to fetch an item from the list in correlation to the number its in the list
print(friends[random_index])
