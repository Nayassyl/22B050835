import re
if re.search('ab{2,3}', input()):
    print("matches")
else:
    print("no matches")