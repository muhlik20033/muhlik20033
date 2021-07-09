def factorial(x):
    f = 1
    while x > 0:
        f *= x
        x = x-1
    print(f)

factorial(int(input()))