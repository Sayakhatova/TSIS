#the length of an array
fruits=['apple', 'banana', 'cherry']
x=len(fruits)
print(x)
print('\n')

#looping array elements
for x in fruits:
    print(x)
print('\n')

#adding array elements(append())
fruits.append('melon')
print(fruits)
print('\n')

#removing array element(pop())
fruits.pop(2)  #at index 2
print(fruits)
print('\n')

#remove certain element
fruits.remove('banana')
print(fruits)
print('\n')