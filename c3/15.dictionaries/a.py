#A dictionary is a collection which is ordered*, changeable and does not allow duplicates
a={'a':1, 'b':2, 'c':5, 'd':[2, 4, 8]}
print(a)
print(a['a'])

x=a.get('d')
print(x)

y=a.keys()
print(y)
a['r']=989
print(y)

z=a.values()
print(z)

c=a.items()
print(c)