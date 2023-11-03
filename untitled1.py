def power_naiive(a, n):
    res = 1
    for _ in range(n):
        res *= a
    return res
def power_divide_conquer(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = power_divide_conquer(a, n // 2)
        return half* half
        half = power_divide_conquer(a, (n - 1) // 2)
        return half * half * a
