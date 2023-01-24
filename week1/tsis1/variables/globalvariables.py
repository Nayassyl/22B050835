x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

def myfunc1():
  x = "fantastic"
  print("Python is " + x)

myfunc1()

print("Python is " + x)


def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is " + x)