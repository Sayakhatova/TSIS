#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3853#1
a=input().split()
m=int(input())
res=[]
for i in range(len(a)):
    res.append(a[i-m])
print(' '.join(res))