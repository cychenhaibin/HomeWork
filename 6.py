import random
n=eval(input())
random.seed(n)
m = random.randint(1,n-1)
list1 = []
list2 = []
for i in range(1, n+1):
    list1.append(i)
print(list1)
for i in list1:
    if i%m==0:
        list1.remove(i)
print(list1)

