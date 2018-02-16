def factorial(n):
    r = n
    while n > 1:
        n -= 1
        r *= n
    return r


print factorial(10)

assert factorial(3) == 6
