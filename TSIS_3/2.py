#https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3835#1
a=input().split()
res=a[0]
for i in a:
    if int(i)>0:
        if res>i:
            res=i
print(res)