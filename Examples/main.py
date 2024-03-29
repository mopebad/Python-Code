import time
x = 1
print("Original value: ", x)
x = x + 1
print("Modified value: ", x)

print("Location: ", id(x))
print("Value: ", x)

# * Basic Mathematical Operations

a = 2
b = 3
print("a =", a)
print("b =", b)

# Addition
c = a + b  # Declaration of c, and assignment of c.
print("a + b =", c)

# Subtraction
c = a - b  # Assignment of c.
print("a - b =", c)

# Multiplication
c = a * b  # Assignment of c.
print("a * b =", c)

# Division
c = a / b  # Assignment of c.
print("a / b =", c)

# Exponentiation
c = a ** b
print("a ** b =", c)

# Modulus
c = a % b
print("a % b =", c)

a = 1  # Integer which means number.
print(type(a))
a = "Hello"  # String which means word.
print(type(a))
a = 3.14  # Float variable which means decimal number.
print(type(a))
a = True  # Boolean variable which means True or False.
print(type(a))
a = None  # NoneType variable which means No value.
print(type(a))


# * Loops

# Example of a while loop:
i = 9
while i > 0:
    print("Hello")
    i -= 1

# Example of a for loop:
for i in range(9):
    print("Hello")
    print(i)

'''
Here we see that the while loop is in the form of:
    while (boolean statement): 
        action

whereas for loop is in the form of: 
    for (iteration):
        action
'''

# * Reference Types

# An example of a list of integers
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# An example of a list of strings
str_list = ["H", "E", "L", "L",  "O"]

lst = [1, "H", False]

# To access a value stored in a list, we need to use the index.
print(num_list[0])  # Output: 0
print(num_list[5])  # Output: 5
print(str_list[4])  # Output: O
# ! Note that all indexes start from 0
print(str_list)


# A dictionary
my_dict = {"name": "Mope", "age": 14, "PR": 500000, "Graduated": False}

# Dictionaries have key-value pairs, so to access a certain value, we need to use the key.
print(f"Name: {my_dict['name']}\nAge: {my_dict['age']}\nPR: {my_dict['PR']}")

'''
Reference types are variables that are instantiated in the heap, whereas 
primitive types (int, float, bool, etc.) are instantiated in the stack.

The stack and the heap are some of the components that makes up the memory, 
whilst the stack is small (space wise) and fast (access speed wise), the heap 
is more spacious but the access speed is relatively slower. 

Since reference types take up more space than primitive types, they will be 
instantiated on the heap, with a pointer that is created in the stack that 
references the actual object that is in the heap.
'''
print("\n")
for i in range(len(str_list)):
    print(f"Iteration {i}: {str_list[i]}")


def count_down(sec: int):
    for seconds in range(sec, 0, -1):
        print(seconds)
        time.sleep(1)


count_down(15)

str_list = ["F", "O", "R", "T", "N", "I", "T", "E"]

print("\n")
for i in range(len(str_list)):
    print(str_list[i])


# If statements:
'''
if the temperature is negative, we will go skiing; 
if it is above 0, we will go biking, and 
if it is too hot (over 25 degrees celsius), we will go swimming
'''

# * Take the temperature from the user.
temperature: int = int(input("Please enter the temperature: "))
activity: str = ""


# * Form the if... elif... else statements.
if (temperature > 25):
    activity = "swimming"
elif (temperature > 0):
    activity = "biking"
else:
    activity = "skiing"

print("The chosen activity: " + activity)
