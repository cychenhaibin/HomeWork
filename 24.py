n = int(input())
i = 1
def move(n, a, b, c):
    global i
    if n == 1:
        print("[STEP{:>4d}] {}->{}".format(i, a, c))
        i += 1
    else:
        move(n-1, a, c, b)
        print("[STEP{:>4d}] {}->{}".format(i, a, c))
        i += 1
        move(n-1, b, a, c)
move(n, 'A', 'B', 'C')
