import re

S,k = input(), input()
m = list(re.finditer(r'(?={})'.format(k), S))
if m:
    print('\n'.join(str((n.start(), n.start() + len(k) - 1)) for n in m))
else:
    print('(-1, -1)')