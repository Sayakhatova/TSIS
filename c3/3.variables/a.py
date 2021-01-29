#variable
x=5
y="Hello World"
print(x)
print(y)

#variables
x=4     #int
x="apple"    #string
print(x)

#to specify the data type
x=str(3)    #it will be str '3'
y=int(3)    #it will be 3
z=float(3)  #it will be 3.0
print(x, y, z)

#to get a data type of variable
x=5
y="apple"
print(type(x))
print(type(y))

x="John"
#same as
y='John'

a=4
A='umbrella'
#A will not overwrite a

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

x, y, z="Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x=y=z=3
print(x+y+z)

fruits=["banana", "apple", "melon"]
x, y, z=fruits
print(x)
print(y)
print(z)

a="hi"
b="John"
print("hello"+b)
print(a+b)
a=b=5
print(a+b)
#"hello"+5 will be mistake

x = "awesome"
def myfunc():
  #global x
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

#to make variable in function use global ( global x )