len("123456")
print(type(123.455))# can check any data type this way in between " " #float
print(type(123))  #int
print(type("Hello")) #str
print(type(False)) #bool

print(int("123") + int("456"))

#print("Number of letters in your name: " + len(input("Enter your name")))




name_of_user = input("Enter your name")
length_of_name = str(len(name_of_user))

print(type("Number of letters in your name: "))
print(type(length_of_name))

print("Number of letters in your name: " + str(len(name_of_user)))
#used str to make len into a string to match the first part