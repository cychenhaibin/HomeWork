def a(b):
    chen=1
    for i in b:
        chen*=i
    return chen
b=list(map(int,input("").split(',')))
chen=a(b)
print(chen)