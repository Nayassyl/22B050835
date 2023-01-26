x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)

x.difference_update(y) #Remove the items that exist in both sets:
print(x)

"""
The difference_update() method is different from the
difference() method, because the difference() method
returns a new set, without the unwanted items, and the
difference_update() method removes the unwanted items 
from the original set.
"""

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)


x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)