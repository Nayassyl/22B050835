import re
a = re.split('_', input())
for elem in a:
    elem = elem.lower()
    print(elem.capitalize(), end = "")