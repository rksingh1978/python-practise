#python strings
x = "learning python from w3cschools"
y = 'strings are powerful in python'
z = '''Python strings can be written in
multiple line within 3 single quotes of 3 double quotes 
'''
print(x)
print(y)
print(z)

# loop through chars in a string using for
for i in x:
    print(i)

# use of in and not in
if "python" in x:
    print("python is present in x")

if "java" not in y:
    print("java is not present in y")

#slicing strings
print(x[2:5])
print(y[0:-5])

# Modify strings
a = "Automation is useful "
b = "AI based automation is future"
print(a.upper())
print(b.lower())
print(a.replace("A","T"))
# used to strip all empty spaces in a string
print(a.strip())

# concatenate strings
a = "Rakesh"
b = "Singh"
print(a+b)
print(a + " " +b)

# format(f) strings
a = "Rakesh"
b = 47
# print(a + b) # will throw an error
c = f"{a} age is {b}"
print(c)

# escape chars
x = "Hello \nWorld!"
print(x)
y = "Hello\tWorld"
print(y)
z = "Hello \rWorld!"
print(z)

# string in-built functions:
# count()
str = "Python is an OOPS language"
print(str.count('t'))

# isalnum()
str = "Python is an OOPS language"
print(str.isalnum())

# isalpha()
str = "Python is an OOPS language"
print(str.isalpha())

# isascii()
str = "Python is an OOPS language"
print(str.isascii())

# isdigit()
str = "Python is an OOPS language"
print(str.isdigit())

# islower()
print("islower() value of a string:")
str = "Python is an OOPS language"
print(str.islower())

# istitle()
print("istitle() value of a str:")
str = "Python is an OOPS language"
print(str.istitle())
str2 = "Rakesh Kumar Singh"
print("istitle() value of a str2:")
print(str2.istitle())

#










