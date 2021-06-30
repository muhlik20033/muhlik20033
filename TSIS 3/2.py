a = list(input().split())
min = 1000
for i in range(len(a)):
    x = int(a[i])
    if x < min and x >= 0:
        min = x
print(min)