def read_file(file, n):
    from itertools import islice
    with open(file) as f:
        for line in islice(f, n):
            print(line)

x = int(input())
read_file('text.txt', x)