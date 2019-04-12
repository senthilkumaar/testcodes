from collections import Counter, OrderedDict

cal=Counter()
s='replacement'
o=OrderedDict().update(s)
print(cal)
for k,v in cal.items():
    if cal[k]>1:
        print(cal[k])