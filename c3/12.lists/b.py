#access items
list=['banana', 'apple', 'melon', 'cherry', 'kiwi', 'mango']
print(list[2])
print(list[-1])
print(list[2:5])
print(list[:4])
print(list[4:])

#change item in list
list[1]='34'
print(list)
list[2:4]=['58', '45']
print(list)
list[:1]=['48', '75']
print(list)
list[5:]=['7']
print(list)