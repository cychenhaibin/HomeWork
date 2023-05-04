i=0
while True:
    try:
        a = 100
        i+=1
        b = int(input())


        if b==a:
            print("you have tried %d times, you win"%i)
            break

        elif b>a:
            print("larger than expected")

        elif b<a:
            print("less than expected")

    except ValueError:
        print("input error")


