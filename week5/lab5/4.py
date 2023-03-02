import re
if re.search('([A-Z][a-z]+)+', input()):
    print("matches")
else:
    print("no matches")