# global var x, as its not in scope of any function or block
x = "Global x"


def test():
    # local var, as its local to test function
    y = "local y"
    print(y)


test()
print(x)

# Below gives name error, as variable y is not available in the scope where its being used!
# print(y)


def test2():
    # though a global var x is defined, this x is considered as priority!
    x = "local x"
    print(x)


test2()
print(x)


def test3():
    global x
    # mentioning this, ensures we use the global var x
    print(x)


test3()
print(x)


def test3():
    global z
    # before this there is no definition of z
    z = "hiiiiii"
    print(z)


test3()
# we make z global from inside its block, so its accessible here as well!
print(z)


def outer():
    a = "asdasdasd"

    def inner():
        nonlocal a
        print(a)

    inner()
    print(a)


outer()
