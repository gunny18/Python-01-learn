# Why EAFP is better than checking for permision or existence ?

# Faster -> Less access into variables to check for permission. Because we just do it
# Clean code -> Handling of cases are much cleaner and code is understandable

def work_on_list_non_pythonic(l, ind):
    if len(l) >= ind+1:
        print(l[ind])
    else:
        print("Missing index")

def work_on_list_pythonic(l, ind):
    try:
        print(l[ind])
    except IndexError as e:
        print(f"Missing index -> {e}")

l = [1,2,3,4]

work_on_list_non_pythonic(l,1)
work_on_list_non_pythonic(l,4)

work_on_list_pythonic(l,1)
work_on_list_pythonic(l,100)