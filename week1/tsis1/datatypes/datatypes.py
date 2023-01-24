x = 5
print(type(x))

x = "Hello World"
print(type(x)) #str

x = 20.5
print(type(x)) #float

x = 1j
print(type(x)) #complex

x = ["apple", "banana", "cherry"]
print(type(x)) #list

x = ("apple", "banana", "cherry")
print(type(x)) #tuple

x = range(6)
print(type(x)) #range

x = {"name" : "John", "age" : 36}
print(type(x)) #dictionary

x = {"apple", "banana", "cherry"}
print(type(x)) #set

x = frozenset({"apple", "banana", "cherry"})
print(type(x)) # frozenset

x = True
print(type(x)) #boolean

x = b"Hello"
print(type(x)) #bytes

x = bytearray(5)
print(type(x)) #bytearray

x = memoryview(bytes(5))
print(type(x)) #memoryview

x = None
print(type(x)) #NoneType