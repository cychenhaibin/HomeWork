def isprime(n):  #判断素数函数
    l=[]
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True


def f(n):        #找小于n的素数并求和
    sum1=0
    list1=[]
    for i in range(3,n+1):
        if isprime(i):
            list1.append(i)

    list2=list1[-1:-11:-1]
    sum1=sum(list2)
    return sum1

p=eval(input())

print(f(p))