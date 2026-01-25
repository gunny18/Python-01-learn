student = {"name": "Alex", "age": 24, "courses": ["Math", "Comp-Sci", "MMA"]}
print(student)

student.update({"age": 26})
print(student)

courses = student.pop("courses")
print(student, courses)
