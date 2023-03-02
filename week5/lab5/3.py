import re
if re.search('[a-z]+_[a-z]', input()):
    print("matches")
else:
    print("no matches")