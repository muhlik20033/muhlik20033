with open('text.txt') as f:
    file = f.read().splitlines()
    print([s.rstrip('\n ') for s in file])