def perfect(x):
    l = []
    for i in range(1, x):
        if x%i==0:
            l.append(i)
    
    if sum(l) == x and (sum(l)+x)/2==x:
        print(x, 'is perfect number')
    else:
        print(x, 'is not perfect number')

    
perfect(int(input()))