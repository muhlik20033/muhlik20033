from collections import Counter

def sample_file(file):
    with open(file) as f:
        return Counter(f.read().split())

print(sample_file('text.txt'))
