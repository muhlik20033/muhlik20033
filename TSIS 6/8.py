l = [1,2,3,3,3,3,4,5]
uni = []
for i in l:
    if i not in uni:
        uni.append(i)

print(uni)