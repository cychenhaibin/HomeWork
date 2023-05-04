dic={"aaa":'123456',"bbb":'888888',"ccc":'333333'}
x=3
n=input()
if n in dic:
    while x>0:
        a=input()
        if a==dic[n]:
            print("Success")
            break
        else:
            x-=1
            if x>0:
                print("Fail,{} Times Left".format(x))
    if x==0:
        print("Login Denied")
else:
    print("Wrong User")