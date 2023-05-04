a,b = map(int,input().split(' '))
i = 0
while(i<=a):
    if(2*i+4*(a-i)!=b):
        i+=1
    else:
        print(i, a-i)
        break
else:
    print("Data Error!")