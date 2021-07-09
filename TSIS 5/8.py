def sample_file(file):
    with open(file, 'r') as f:
        words = f.read().split()
    max_l = len(max(words, key = len))
    return[w for w in words if len(w) == max_l]

print(sample_file('text.txt'))