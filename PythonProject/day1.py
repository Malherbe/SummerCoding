for n in range(2,19):
    for x in range(2,n):
        if n%x == 0:
            print(n, 'equals', x, 'X', n//x)
            break
    else:
        print(n, "is a prime number.")


def fibonacci(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b =b, a+b
    return result

print(fibonacci(200))


