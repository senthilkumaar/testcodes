sting='Welcome to the jungle'
count =0
flag= True
# sting+='@'
# strings=sting.replace(" ","")
# strings=strings+'@'
# print(strings)
# while strings[count] != '\n':
#     count+=1
#     if strings[count]=='@':
#         break
#
# print(count-1)

# while sting[count] !='@':
#     count += 1
#
# print(count)



i=0
while sting[i] == sting:

    if flag == False and sting[i]==' ':
        count += 1
    elif sting[i] == ' ':
        flag= True
    else:
        flag = False
    i=i+1

print(count)

