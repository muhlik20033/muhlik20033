def file_read(fname):
        with open(fname) as f:  
                l = f.readlines()
                print(len(l))

file_read('text.txt')