fd1 = open("in162.txt", "r")
sum = 0
count = 0
line = fd1.readline()    # 读入一行字符串
weight = list(line.split()) # 以空格提前字符串
for item in weight:
    sum += eval(item)*0.454
    count += 1
    if count == 10:
        break
fd2 = open("out162.txt", 'w')
fd2.write("%.2f" % sum)
fd1.close()
fd2.close()

