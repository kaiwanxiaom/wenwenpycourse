
## 函数

def f(a, b):
    return a + b

## 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

