def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(10))
print(fibonacci(20))