def is_prime(n):
    """判断是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if n % 2 != 0:  # 如果是奇数，直接输出 'Data error!'
    print('Data error!')
else:
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print('N = {} + {}'.format(i, n - i))
            break  # 输出最小解即可，直接退出循环。