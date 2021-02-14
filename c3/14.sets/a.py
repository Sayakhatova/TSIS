# set is a collection which is both unordered and unindexed
set1={'a', 'c', 'r', 'e', 'a', 't', 'r'}
a= set(('banana', 'cherry', 'melon'))
print(set1)   #no dupplicates
print(a)
print('\n')

#You cannot access items in a set by referring to an index or a key
s={1, 5, 6, 9}
for x in s:
    print(x)

# add() method
s.add('banana')
print(s)