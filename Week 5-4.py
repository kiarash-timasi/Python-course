def func(x):
    y = x ** 3 - x ** 2 + 2
    return y


def derifunc(x):
    y = 3 * x * x - 2 * x
    return y


def newtonraphson(x):
    h = func(x) / derifunc(x)
    while abs(h) >= 0.001:
        h = func(x) / derifunc(x)
        x = x - h
    print("The Roots of equation is: %4f" % x)
c = 20
newtonraphson(c)
