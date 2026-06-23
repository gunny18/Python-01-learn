# Why do we mean by pythonic?
# Duck typing and EAFP are 2 things that define the pythonic way to write code

# Duck typing
# If it walks like a duck and talks like a duck it is a duck!
# Python says don't check if an object is of a certain type
# 2 objects are treated as same by python if it supports the behavior (method) we want from it.
# Does not mean both objects have to be of a certain typt to exhibit that behaviour.
# Point is in pythonic way, dont check behavior existence by checking type.
# Just perform it. If it doesn not exist handle the error


class Duck:
    def quack(self):
        print("A duck is quacking")

    def fly(self):
        print("A duck is flying")

class Person:
    def quack(self):
        print("A person is quacking like a duck")

    def fly(self):
        print("A person is flying like a duck")


# Forcefully restricting actions only if its type Duck
def fly_and_quack_non_pythonic(thing):
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("The object has to be a duck!")

# Say now instead of restricting we are explicitly checking if the attributes exist and is callable
def fly_and_quack_pythonic(thing):
        thing.quack()
        thing.fly()

d = Duck()
p = Person()

fly_and_quack_non_pythonic(d)
fly_and_quack_non_pythonic(p)

fly_and_quack_pythonic(d)
fly_and_quack_pythonic(p)
