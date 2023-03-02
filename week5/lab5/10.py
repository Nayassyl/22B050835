import re
a = re.findall('.[^A-Z]*', input())
str = ""
for elem in a:
    str += elem.lower() + "_"
print(str[:-1])