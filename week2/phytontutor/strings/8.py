s = input()
a = s[:s.find('h')]
b = s[s.rfind('h') + 1 :]
c = s[s.find('h'):s.rfind('h') + 1]
print(a + c[::-1] + b)
