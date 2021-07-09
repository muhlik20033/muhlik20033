s = "1234abcd"

def re(st):
    s_r = ''
    quan = len(st)
    while quan > 0:
        s_r += st[quan-1]
        quan = quan-1
    print(s_r)

re(s)