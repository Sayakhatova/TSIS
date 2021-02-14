#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3840#1
"""
a=input().split()
a.reverse()
print(a)
"""
a=input().split()
res=[]
for i in a:
    res.insert(0, i)
print(' '.join(res))