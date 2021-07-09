import os

def sample_file(file):
    file_size = os.stat(file).st_size
    return file_size

print(sample_file('text.txt'))