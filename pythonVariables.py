# Simple variables are created by assigning it's values
x = 3
y = 5
z = 7
print(x, y, z)

# variables are assigned as a list as well
x, y, z = {"apple", "banana", "pear"}
print(x)
print(y)
print(z)
print(x + y + z)

# unpacking
fruits = {"apple", "banana", "pear"}
x, y, z = fruits
print(x)

# type of variables
x = 5
y = "apple"
print(type(x), type(y))

# adding 2 variables
x = 2
y = 3
print(x + y)

# local (inside a function) vs global variable (outside a function)
x = 5  # global variable

def func():
    x = 7  # local variable
    print("local value of x is:")
    print(x)
func()
print("global value of x is:")
print(x)

# local value inside a function can be made global by terming it as global
