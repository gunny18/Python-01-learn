# lists and tuples work same during sorting!

li = [9, 1, 3, 5, 4, 2, 7, 6, 8]

# Methods sorts the list in place!
# new_li = li.sort()

new_li = sorted(li)
print(li, new_li)

rev_new_li = sorted(li, reverse=True)
print(rev_new_li)

# Passing key!
t = sorted([-1, 2, 3, 5, 4, -2, 3])
print(t)

t = sorted([-1, 2, 3, 5, 4, -2, 3], key=abs)
print(t)

# Sorting objects! - dicts, classes, etc!
students = [
    {"name": "Alex", "age": 12},
    {"name": "Wu Shang", "age": 10},
    {"name": "Sarabia", "age": 18},
]


def sort_by(e):
    # return e["name"]
    return e["age"]


w = sorted(students, key=sort_by)
print(w)

w = sorted(students, key=sort_by, reverse=True)
print(w)


w = sorted(students, key=lambda e: e["age"])
print(w)


# ------------------------ Works on class objects! --------------------------------
# from operator import attrgetter

# w = sorted(students, key=attrgetter("age"))
# print(w)
