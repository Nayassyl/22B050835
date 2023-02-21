import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

import mymodule as mx

a = mx.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)

from mymodule import person2

print (person1["age"])