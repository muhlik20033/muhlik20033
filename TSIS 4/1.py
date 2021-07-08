import re

for _ in range(int(input())):
    print(bool(re.search('^[+-]?\d*\.\d+$', input())))