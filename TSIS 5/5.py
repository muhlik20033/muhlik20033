def file_read(fname):
        with open(fname) as f:  
                l = f.readlines()
                print(l)

file_read('text.txt')