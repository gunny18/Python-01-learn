read_size = 1096
with open("img.png", "rb") as rf:
    with open("img_copy.png", "wb") as wf:
        c = rf.read(read_size)
        while len(c) > 0:
            wf.write(c)
            c = rf.read(read_size)
