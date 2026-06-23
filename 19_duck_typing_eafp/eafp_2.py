# The concept of EAFP is applicable in any puthon code
# Say we are working on dictionary

def work_on_dict_non_pythonic(p):
    if "name" in p and "age" in p and "courses" in p:
        print("I am {name}. I am {age} years old. My subjects are {courses}".format(**p))
    else:
        print("Missing keys")

def work_on_dict_pythonic(p):
    try:
        print("I am {name}. I am {age} years old. My subjects are {courses}".format(**p))
    except KeyError as e:
        print(f"Missing key {e}")


person_1 = {"name":"Alex","age":12,"courses":["Math","CompSci"]}
person_2 = {"name":"Alex","age":12}

work_on_dict_non_pythonic(person_1)
work_on_dict_non_pythonic(person_2)

work_on_dict_pythonic(person_1)
work_on_dict_pythonic(person_2)