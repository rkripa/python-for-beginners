
print("\nFile Name: {} Module Name: {}".format( __file__, __name__))


def foo():
    print("In foobar.py::foo()")

def bar():
    print("In foobar.py::bar()")

def spam():
    print("In foobar.py::spam()")

print("Symbol Table {} {}:".format(__file__, dir())) # names in current scope
