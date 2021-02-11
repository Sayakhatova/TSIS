#loop list
list=[47, 45, 187, 646, 7894]
for x in list:
    print(x, end=' ')
print('\n')
for i in range(len(list)):
    print(list[i], end=' ')
print('\n')

list1=['banana', 'cherry', 'strawberry']
i=0
while i<len(list1):
    print(list1[i], end='   ')
    i+=1
print('\n')

#another method
list2=[458, 547, 2168, 68, 587, 455]
[print(x) for x in list2]