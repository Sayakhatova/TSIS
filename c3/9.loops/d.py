#python for loops
fruits=['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
print('\n')

for x in 'banana':
    print(x)
print('\n')

#the break statement
fruits=['apple', 'banana', 'cherry']
for x in fruits:
    if x=='banana':
        break
    print(x)
print('\n')

fruits=['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x=='banana':
        break
print('\n')

#the continue statement
fruits=['apple', 'banana', 'cherry']
for x in fruits:
    if x=='banana':
        continue
    print(x)
print('\n')
