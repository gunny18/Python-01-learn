with open("test.txt", "r") as rf:
    with open("test1_copy.txt", "w") as wf:
        for c in rf:
            wf.write(c)
