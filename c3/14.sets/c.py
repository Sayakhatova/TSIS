#keep only duplicates
a={'a', 'b', 'c', 't', 'd'}
b={'b', 'v', 'j', 'd'}
a.intersection_update(b) #or just a.intersection(b)
print(a)

#without dupplicates
a1={'a', 'b', 'c', 't', 'd'}
b1={'b', 'v', 'j', 'd'}
a1.symmetric_difference_update(b1)
print(a1)