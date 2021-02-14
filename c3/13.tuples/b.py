#change tuple values
x=('apple', 'banana', 'strawberry', 'cherry')
y=list(x)
y[1]='kiwi'
y.append('orange')      #add element
y.remove('apple')       #remove element
x=tuple(y)
print(x)
print('\n')

#unpacking tuples
fruits=('apple', 'banana', 'cherry')
(aa, ab, ac)=fruits
print(aa, ab, ac, '\n')

#or
fruits1=('banana', 'apple', 'melon', 'strawberry', 'cherry')
(aa, *ab, ac)=fruits1
print(aa)
print(ab)
print(ac)