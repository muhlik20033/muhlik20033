s = 'The quick Brow Fox'
l, u = 0, 0
for i in s:
    if i.islower():
        l += 1
    elif i.isupper():
        u += 1
    else:
        pass


print('Number of lower letters:', l)
print('Number of upper letters:', u)