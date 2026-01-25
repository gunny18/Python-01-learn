with open("test2.txt", "w") as wf:
    wf.write("Hellooooo")

with open("test3.txt", "w") as wf:
    wf.write("Test")
    wf.seek(0)
    wf.write("T")
