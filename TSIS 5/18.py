def sample_file(file):
    with open(file) as f:
        txt = f.read()
        txt = txt.replace(',', ' ')
        print(len(txt.split(' ')))

sample_file('text.txt')