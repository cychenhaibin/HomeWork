n = eval(input())
arr = [[0 for i in range(n)] for j in range(n)] 
max = n*n   
num = 1
x = 0
y = 0
while num <= max:
    for i in range(n): 
        arr[x][y] = num
        num += 1
        y += 1
    y -= 1  
    n -= 1  
    x += 1
    for i in range(n): 
        arr[x][y] = num
        num += 1
        x += 1
    x -= 1
    y -= 1  
    for i in range(n): 
        arr[x][y] = num
        y -= 1
        num += 1
    y += 1
    x -= 1  
    n -= 1
    for i in range(n):
        arr[x][y] = num
        x -= 1
        num += 1
    x += 1  
    y += 1
# print(arr)
fd = open("file.out", 'w')
for i in arr:
    for j in i:
        fd.write("%5d"%j)
    fd.write("\n")

