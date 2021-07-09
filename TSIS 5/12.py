l = ['sofa', 'table', 'chair', 'wardrobe']

with open('text.txt', 'w') as f:
        for i in l:
            f.write('%s ' % i)

txt = open('text.txt')
print(txt.read())