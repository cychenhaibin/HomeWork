def triangle(n):
    temp = []
    if n == 1:
        temp.append(1)
        return temp
    lis.append(triangle(n - 1))
    temp.append(1)
    for i in range(n - 2):
        temp.append(lis[n - 2][i] + lis[n - 2][i + 1])
    temp.append(1)
    return temp
 
def printf(n,blacklen):
    for i in range(n):
        print(' ' * (blacklen * (n - i) + 1) ,end = '')
        for j in range(len(lis[i])):
            print(' ' * (blacklen - len(str(lis[i][j]))),end = '')
            print(lis[i][j],end = ' ' * blacklen)
        print()    
 
n = int(input())
lis = []
lis.append(triangle(n))
maxNumber = lis[n - 1][n // 2]
blacklen = len(str(maxNumber))
printf(n,blacklen)
