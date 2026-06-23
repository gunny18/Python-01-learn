name = "Alex"
print(id(name))

age = 43
print(id(age))

# Same string, hence python does optimization under the hood to point name2 to same address as name variable as they represent the same string!
name2 = "Alex"
print(id(name2))

# Checks the object identity, i.e, id(name) == id(name2). Will be true in this case
print(name is name2)

# Since i am performing an operation on name2, and I have not directly referenced name and name2, now they will be different!
# Changing name2 will not impact name as they are not aliases! Hence now python allocates name2 to a diff memory location!
name2 = name2.lower()
print(name, id(name), name2, id(name2))

# Checks the object identity, i.e, id(name) == id(name2). Will be false in this case
print(name is name2)

# for list, it is not the case!. Id will be same only if its referenced or alias to the original list!
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b))

# Referencing b to a. b is now an alias to a.
a = b
print(id(a), id(b))

# for tuple, its same as strings! Reason - tuple and string are immutable! List is Mutable
c = (1, 2)
d = (1, 2)
print(id(c), id(d))

# So this above experiment and mem allocation depends on the data type being mutable or immutable!
