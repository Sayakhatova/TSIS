a='Hello'
print(a)
a="""It    
was 
a good
day"""
print(a,'\n')

#string as arrray
a='pineapple'
print(a[1],'\n')

#loop through string
for x in 'banana':
    print(x)
print('\n')

#string lenth
a='Hello world'
print(len(a))
print('\n')

#substr
a='the best things in life are free'
print('free' in a) 
#or
if 'free' in a:
    print('\nYes\n')

#if not substr
a='the best things in life are free'
print('best' not in a)
if 'apple' not in a:
    print('\nNO')