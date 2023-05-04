def getText():
    # f=open("k.txt", "r")
    f=open("sensor-data-1k.txt", "r")
    total=0
    for i in range(1000):
        info=f.readline()
        time,time2,tem,wet,light,ele=info.split()
        total=total+eval(light)
    return total/1000
print("{:.2f}".format(getText()))

