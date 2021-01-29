print(10>9)
print(10==9)
print(10<9)
print('\n')

#if else
a=49
b=78
if b>a:
    print('b is greater')
else:
    print('b is less')
print('\n')

"""
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print('\n')

#check if object is int or not
x = 200
print(isinstance(x, int))