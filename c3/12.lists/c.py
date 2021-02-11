#insert items to list insert()
list=[47, 48, 95, 65, 487]
list.insert(2, 'melon')
print(list)

#to add to the end use append()
list.append('yellow')
print(list, '\n')

#to add elements from one list to another extend()
list1=[]
list1.extend(list)
print(list)
print(list1, '\n')

#remove specified item remove()
list1.remove(487)
print(list1)

#remove specified item by index  pop()
list1.pop(4)     #pop()   removes last item
print(list1)

#method del
del list1[2]   
print(list1)

del list1 #delete the list completely

#method clear()  will empty the list
list.clear()
print(list)