# Another reason EAFP is better ?
# Race condition

import os

file = "/tmp/some_file.txt"

def access_file_with_race_condition():
    if os.access(file, os.R_OK): # Checking if file can be accessed and read from
        with open(file) as f: # What if exactly when we are at this line, file becomes in accessible. It will cause errors
            print(f.read()) # So this will cause a race condition, all because we waited for permission instead of doing it.
    else:
        print("File cannot be accessed")

# Here no race condition. Yes it can happen file cannot be accessed, but that is handled!
# And no chance we will run into race condition as above
def access_file():
    try:
        f = open(file)
    except IOError as e:
        print(f"File cannot be accessed -> {e}")
    else:
        with f:
            print(f.read())

access_file_with_race_condition()
access_file()