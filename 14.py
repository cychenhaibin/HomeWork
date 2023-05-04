flag = 1
for i in range(11,30):
    num1=i**3
    num2=i**4
    str1 = str(num1)+str(num2)
    if len(str1) == 10:
        for j in range(10):
            if str1.count(str(j)) != 1:
                flag = 0
                break
        if flag == 1:
            print(i)


