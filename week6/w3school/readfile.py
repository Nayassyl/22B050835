f = open("C:\python2\week6\w3school\demofile.txt", "r")
print(f.read())

f = open("C:\python2\week6\w3school\demofile.txt", "r")
print(f.read(5))
f = open("C:\python2\week6\w3school\demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("C:\python2\week6\w3school\demofile.txt", "r")
for x in f:
  print(x)
f.close()
