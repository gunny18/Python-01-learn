# All basics present in nebo notebook

courses = ["History", "Art", "Math"]

# join
courses_str = " - ".join(courses)
print(courses_str)


# split str
courses_list = courses_str.split(" ")
print(courses_list)

# enumerate
for index, course in enumerate(courses, start=2):
    print(index, course)

# mthods
courses.insert(1, "Mog")
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

print(len(courses))

sorted_courses = sorted(courses_list)
print(sorted_courses)

courses.index("asdasd")
