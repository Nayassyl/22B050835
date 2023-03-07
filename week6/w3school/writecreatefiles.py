"""
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

f = open("C:\python2\week6\w3school\demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("C:\python2\week6\w3school\demofile2.txt", "r")
print(f.read())


f = open("C:\python2\week6\w3school\demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("C:\python2\week6\w3school\demofile3.txt", "r")
print(f.read())



f = open("C:\python2\week6\w3school\myfile.txt", "x")
f = open("C:\python2\week6\w3school\myfile.txt", "w")
