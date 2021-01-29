#find() method(substr)
txt='Hello, welcome to my world'
x=txt.find('welcome')
print(x)
print(txt.find('l', 5, 10))
print('\n')

#join() method
a=('banana', 'apple', 'cherry')
x="#".join(a)
print(x)
print('\n')

a={'name':'John', 'country':'Norway'}
b='test'
x=b.join(a)
print(x)
print('\n')

#lstrip() method
txt='banana'
x=txt.lstrip("b")
print(x)
print('of all fruits', x, 'is my favorite')
print('\n')