# EAFP - Easier to ask for forgiveness than permission
# It says if you want to do something, just do it.
# If it does not work out, handle exception
# It is better than checking if it will work out and then do what you want
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


# To do anything, I am asking permission to do it, eve before I can do it.
# Leads to a lot of permission code
# Here to handle if permission not given, I need to write more code
# This is also called -> Look before you leak (LBYL)
def do_somethings_non_pythonic(thing):
    if hasattr(thing,"quack"):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing,"fly"):
        if callable(thing.fly):
            thing.fly()
    if hasattr(thing,"bark"):
        if callable(thing.bark):
            thing.bark()

# I just do the things I want. If not possible I handle the appropriate errors, the way I want
def do_somethings_pythonic(thing):
        try:
            thing.quack()
            thing.fly()
            thing.bark()
        except AttributeError as e:
            print(f"Missing attribute {e}")

d = Duck()
p = Person()

do_somethings_non_pythonic(d)
do_somethings_non_pythonic(p)

do_somethings_pythonic(d)
do_somethings_pythonic(p)