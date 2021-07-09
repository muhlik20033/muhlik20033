import os

def sample_file(file, n):
    bufsize = 8192
    f_size = os.stat(file).st_size
    iter = 0
    with open(file) as f:
        if bufsize > f_size:
            bufsize = f_size-1
            list = []
            while True:
                iter += 1
                f.seek(f_size-bufsize*iter)
                list.extend(f.readlines())
                if len(list) >= n or f.tell() == 0:
                    print(''.join(list[-n:]))
                    break

x = int(input())
sample_file('text.txt', x)