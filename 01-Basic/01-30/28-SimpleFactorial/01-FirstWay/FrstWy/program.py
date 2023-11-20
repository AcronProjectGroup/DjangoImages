# 3! = 1 * 2 * 3
# 5! = 1 * 2 * 3 * 4 * 5


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4))