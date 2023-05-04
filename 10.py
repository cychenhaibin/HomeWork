
def b(a):

    d = []

    avg=sum(a)/len(a)

    for i in range(len(a)):
        if a[i]>avg:
            d.append(a[i])

    return avg,d
a=input("Please input numbers,and press the Enter to end.(gap with ,)\n").split(',')
tuple=list(map(int,a))
z=b(tuple)
print(z)

