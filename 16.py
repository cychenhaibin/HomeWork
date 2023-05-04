a = int(input())
sum1 = 0
for i in range(1,a+1):
    chen = 1
    for j in range(1,i+1):
        chen = chen*j
    sum1 = chen + sum1
print(sum1)

