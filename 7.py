a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
a.extend(b)
c=[]
for i in a:
    if i not in c:
        c.append(i)
c.sort()
str1=""
for i in c:
    str1+=str(i)

print(str1)