import random

with open('text.txt') as f:
    file = f.read().splitlines()
    print(random.choice(file))