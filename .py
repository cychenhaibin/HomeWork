a,b,c=map(float,input().split())
d=b**2-4*a*c
if d>0:
    x1=(b+d**0.5)/(-2*a)
    x2=(b-d**0.5)/(-2*a)
    if x1>x2:
        print("{:.2f} {:.2f}".format(x1,x2))
    elif x2>x1:
        print("{:.2f} {:.2f}".format(x2,x1))
elif d==0:
    x=b/-2*a
    print("{:.2f} {:.2f}".format(x,x))
elif d<0:
    print("No")