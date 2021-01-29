#else in for loop
for x in range(6):
    print(x)
else:
    print('finally finished')
print('\n')

#after break else will not work
for x in range(6):
    if x==3: break
    print(x)
else:
    print('finally finished')
print('\n')

#nested loops
adj=['red', 'big', 'tasty']
fruits=['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)
print('\n')