#add two sets  update()  method   or   union()
a={1, 7, 6, 9}
b={'b', 'c', 'h'}
a.update(b)
print(a)
print('\n')

#remove        remove(), discard() method   the last item pop()  method
b.discard('h')
print(b)
x=b.pop()
print(x, b)