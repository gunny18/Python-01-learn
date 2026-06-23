import os

print(os.getcwd())

os.chdir("C:/Users/USER/Desktop")

print(os.getcwd())

os.mkdir("test")

os.makedirs("test2/test3/test4")

print(os.listdir())


if os.path.exists("ather_insurance.pdf") and os.path.isfile("ather_insurance.pdf"):
    os.rename("ather_insurance.pdf", "Ather Insurance.pdf")

print(os.listdir())

print(os.stat("Ather Insurance.pdf"))


for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("DIRPATH", dirpath)
    print("DIRNAMES", dirnames)
    print("FILENAMES", filenames)


os.rmdir("test")

os.removedirs("test2/test3/test4")

print(os.listdir())

print(os.path.basename(os.path.join(os.getcwd(), "Ather Insurance.pdf")))
print(os.path.dirname(os.path.join(os.getcwd(), "Ather Insurance.pdf")))
print(os.path.split(os.path.join(os.getcwd(), "Ather Insurance.pdf")))
print(os.path.splitext(os.path.join(os.getcwd(), "Ather Insurance.pdf")))
