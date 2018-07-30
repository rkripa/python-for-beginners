print("File Name: {}\nModule Name: {}".format( __file__, __name__))   # print __file__ and __name__

def spam():
    print("In spam.py::spam()")

print("\nSymbol Table 1 {}\n{}:".format(__file__, dir())) # names in current scope 

from foobar import foo, bar

from foobar import spam as eggs

print("\nSymbol Table 2 {}\n{}:".format(__file__, dir())) # names in current scope after import of foobar

print()

foo()    # call functions in foobar.py as foo()

bar()

spam()

eggs()
