#encode() method
txt='My name is Ståle'
x=txt.encode()
print(x)
print('\n')

#endswith() method. Check if the string ends with .
txt='Hello, welcome to my world.'
x=txt.endswith('.')
print(x)
print('\n')

#check if this string exists in position 5-11
txt='Hello, welcome to my world.'
x=txt.endswith('my world.', 5, 11)
print(x)
print('\n')

#expandtabs() method
txt='h\te\tl\tl\to'
x=txt.expandtabs(2)
print(x)
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))