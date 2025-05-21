import random
import my_module

print(my_module.my_favorite_number)

# random_number_0_to_1 = random.random() * 10
# print(round((random_number_0_to_1),2))#this prints numbers between 0 ans 10 not including those
#
# random_float = random.uniform(0, 10) #these will print number 1-10 including those
# print(random_float)

random_integer = random.randint(0,1)
print(random_integer)
if random_integer == 0:
    print("heads")
else:
    print("Tails")

