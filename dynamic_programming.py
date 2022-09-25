def fibonacci(n, mem={}):
    if n==1 or n==2:
        return 1
    
    if n not in mem:
        mem[n] = fibonacci(n-1) + fibonacci(n-2)

    return mem[n]

#v = fibonacci(35)
#print(v)

def best_fibonacci(n):
    if n==1 or n==2:
        return 1

    mem = {0:1, 1:1, 2:1}
    for i in range (2, n + 1):
        mem[i] = mem [i - 1] + mem [i - 2]

    return mem[n - 1]


v = best_fibonacci(35)
print(v)    