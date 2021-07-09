with open('text.txt') as f, open('a.txt') as fi:
    for i, j in zip(f, fi):
        print(i+j)