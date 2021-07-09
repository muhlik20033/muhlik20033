def sample_file(file):
    with open(file, 'w') as f:
        f.write('hello everybody')
    txt = open(file)
    print(txt.read())

sample_file('text.txt')