def fibonacci(num):
    if (num <= 1):
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)

fib = fibonacci(1)
print(fib)
#big O 2^n