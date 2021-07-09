import glob

l = []
files = glob.glob("*.txt")
for f in files:
    with open(f) as x:
        text = x.read()
        l.append(text) 

print(l)