#new list   or  copy()  newlist=list.copy()     or list()   newlist=list(list2)
list=['strawberry', 'banana', 'cherry', 'kiwi', 'apple', 'mango']
newlist=[x for x in list if 'a' in x]
print(newlist)

#method reverse()
newlist.reverse()
print(newlist)
print('\n')

#method sort()
list.sort()
print(list)
list.sort(reverse=True)
print(list)