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

#concatenate strings


