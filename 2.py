a = 0
b = 0
sum = 0
n = 0
c = 1
while c != 0 :
    c = eval(input(""))
    sum = sum + c
    n += 1
    if c < 0:
        a += 1
    else:
        b += 1
avg = sum/(n-1)
print(avg)
print(b-1)
print(a)