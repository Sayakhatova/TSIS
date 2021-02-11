#passing a list
def a(food):
    for x in food:
        print(x)
fruits=["banana", "apple", "melon"]
a(fruits)
print('\n')

#returning values
def b(x):
    return 5*x
b(5)
b(9)
b(3)
print('\n')

#recursion
def c(k):
    if k>0:
        result=k+c(k-1)
        print(result)
    else:
        result=0
    return result
print('\n\nresults: ')
c(6)