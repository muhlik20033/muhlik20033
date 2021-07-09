def sample_file(file):
    array = []
    with open(file, 'r') as f:
        for i in f:
            array.append(i)
        print(array)

sample_file('text.txt')