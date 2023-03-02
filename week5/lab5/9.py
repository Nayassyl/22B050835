import re
a = re.findall('.[^A-Z]*', input())
for elem in a:
    print(elem, end = " ")