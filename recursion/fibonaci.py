# 1 2 3 4 5


def fibonacci(n):
    if(n <= 1):
        return 1
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))


for i in range(1, 11):
    print(i, fibonacci(i))