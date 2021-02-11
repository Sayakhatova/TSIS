#calling a function
def a():
    print("hello world")
a()
print("\n")

#arguments
def f(name):
    print("hello " + name + " !")
f("Suzy")
f("Jack")
print('\n')

#number of arguments
def h(a, b):
    print(a + " " + b)
h('Jack', 'Suzy')
print('\n')

#*args
def p(*kids):
    print("the youngest one is " + kids[2])
p('Tony', 'Jack', 'Lola')

"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
"""