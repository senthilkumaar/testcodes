import re

str='rajan@gmai@lmelf.co.in'
# str = 'welcome to the world by niran@gmail.com rajan@gmail@melf.co.in. ' \
#       'sean conary acted as a first james bond james007@mi6.co.uk  '
# if re.search(r'^[a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$',str):
# if re.search(r'\b(\d{10})\b', str):
# if re.search(r'^[^@]+\@[^@\.]+\.(?:com|co|in|us)(?:\.[a-z]{2,3})?$', str):
#     print("valid email id")
# else:
#     print("not a valid number")
# va= re.search(r'(.*?)rediff',str)
# print(va.group(1))




# for item in list(str.split(' ')):
#     print(item)
#     if re.match(r'^[a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$',item):
#         res= re.findall(r'^[^@]+\@[^\.]+\.(?:com|co|in|us|uk)(?:\.[a-z]{2,3})?$',item)
#         print(res)
#my method
# for item in list(str.split(' ')):
#     # print(item)
#     if re.match(r'^\S+@\S+',item):
#         result= re.findall(r'^[^A-Z_0-9]+(\.[_a-z0-9-]+)*@([^A-Z_@])+(\.[_a-z0-9-])*(\.[a-z]{2,3})?$',item)
#         print(result)

# result= re.match(r'^[^A-Z_0-9]+(\.[_a-z0-9-]+)*@[^@A-Z_]+(\.[_a-z0-9-])*(\.[a-z]{2,3})?$',str)
# print(result.group(0))

pattern = re.compile(r'^[a-z0-9]+(\.[a-z0-9W])*@[a-z0-9]+(\.[a-z0-9]+)*')
print(pattern.search(str))