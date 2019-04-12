'''

s = 'we1come @t th* HC$'
splitstr = list(s)
count = 0
schar = ['#', '@', '!', '$', '%', '*', 1]
for i in range(len(splitstr)):
    for j in range(len(schar)):
        if splitstr[i] == schar[j]:
            count += 1
            splitstr[i] = count

str1 = ''.join(str(e) for e in splitstr)
print(str1)

'''
s = 'we1come @t th* HC$'
count = 0
sy=''
for item in s:
    if item.isalpha() or item.isspace():
        sy+=item
    else:
        count += 1
        sy+=str(count)

print(sy)


