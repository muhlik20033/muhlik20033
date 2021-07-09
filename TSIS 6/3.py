def multi(a: tuple):
    n = 1
    for i in a:
        n *= i
    print(n)

multi((8, 2, 3, -1, 7))