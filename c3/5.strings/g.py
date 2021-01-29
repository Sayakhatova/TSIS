#capitalize() method. make the first letter upper
txt='hello'
print(txt.capitalize())
print('\n')

#casefold() method. make the string lower case
txt="Hello, And Welcome"
x=txt.casefold()
print(x)
print('\n')

#center() method. taking up the space 
txt='banana'
x=txt.center(20)
print(x)
print(txt.center(15, 'O'))
print('\n')

#count() method
txt='I love apples, apple are my favorite fruit'
x=txt.count('apple')
print(x)
y=txt.count('apple', 10, 24)
print(y)