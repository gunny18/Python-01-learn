def say_name(*args, **kwargs):
    print(args)
    print(kwargs)


say_name(1, "Helllo", age=23, courses=["Math", "Arts"])

args_list = (1, "Helllooo")
kwargs_list = {"age": 23, "courses": ["Math", "Comp-Sci"]}

# both treated as args only!
say_name(args_list, kwargs_list)

# must be unpacked if we want to pass as args and kwargs!
say_name(*args_list, **kwargs_list)
