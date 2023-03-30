x = 1
print("Original value: ", x)
x = x + 1
print("Modified value: ", x)

print("Location: ", id(x))
print("Value: ", x)

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

'''
Here we see that the while loop is in the form of:
    while (boolean statement): 
        action

whereas for loop is in the form of: 
    for (iteration):
        action
'''
