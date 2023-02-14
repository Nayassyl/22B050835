def capitalize(list):
    str = ""
    for i in list:
        str += i.capitalize() + " "
    return str
s = [ s for s in input().split()]
print(capitalize(s))
