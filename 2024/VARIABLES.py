# variable = a container for a value.

# String variable
name = "string"
print(type(name))

# if (type(name) == str):
#     print("This is a string")

first_name = "first"
last_name = "last"
full_name = first_name + " " + last_name

print(full_name)

# int variable

age = 88
age += 1
print (type(age))

print(str(age) + full_name)


# float datatype

height = 250.5 
print("Height is: " + str(height)+"cm")
#print(type(height))


# boolean datatype

SWITCH = False
print("Is switch on: " + str(SWITCH))
# print(type(SWITCH))

# multiple assignment

# name = "name"
# age = 21
# alive = True



name,age,alive = "name",21,True

# print(name, age, alive)
print(name)
print(age)
print(alive)


num1 = num2 = num3 = num4 = 30
lNums = [num1, num2, num3, num4]

for i in lNums:
    print(i)
