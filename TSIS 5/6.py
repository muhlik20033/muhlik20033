def sample_file(file):
    with open(file, 'r') as f:
        l = f.readlines()
        print(l)

sample_file('text.txt')