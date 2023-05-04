a=input("What is the temperature?")
try:
    if a[-1] in ['F','f']:
        C=int((eval(a[0:-1])-32)/1.8)
        print("The converted temperature is {:d}C".format(C))

    elif a[-1] in ['C','c']:
        F = int(1.8*eval(a[0:-1])+32)
        print("The converted temperature is {:d}F".format(F))
    else:
        print("End with 'C','c','F','f'")
except:
    print("Input error")


