# Usual file open
f = open("test.txt", "r")
print(f.name)
f.close()

# with context managers!
with open("test.txt", "r") as f1:
    print(f1.name, f1.closed)

# No effect!, as context manager already closed the file
print(f1.closed)
f1.close()


with open("test.txt", "r") as f1:
    content = f1.read()
    print(content)

with open("test.txt", "r") as f1:
    content = f1.readlines()
    print(content)

with open("test.txt", "r") as f1:
    content = f1.readline()
    print(content, end="")
    content = f1.readline()
    print(content, end="")
    content = f1.readline()
    print(content, end="")


with open("test.txt", "r") as f1:
    for line in f1:
        print(line, end="")

with open("test.txt", "r") as f1:
    size_to_read = 10
    ct = f1.read(size_to_read)
    while len(ct) > 0:
        print(ct, end="**")
        ct = f1.read(size_to_read)
