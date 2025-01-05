def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

fib_482 = fib(482)
print(fib_482)
fib_last_3 = fib_482 % 1000
print(fib_last_3)
