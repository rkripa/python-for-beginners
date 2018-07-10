
print("\nFile Name: {} Module Name: {}".format( __file__, __name__))


def foo():
    print("In foo")

def bar():
    print("In bar")

print("Symbol Table {} {}:".format(__file__, dir())) # names in current scope
