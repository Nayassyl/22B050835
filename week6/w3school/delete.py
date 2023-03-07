import os
if os.path.exists("C:\python2\week6\w3school\myfile.txt"):
  os.remove("C:\python2\week6\w3school\myfile.txt")
else:
  print("File does not exist!")

if os.path.exists("C:\python2\myfolder"):
  os.rmdir("C:\python2\myfolder")
else:
  print("Folder does not exist!")
