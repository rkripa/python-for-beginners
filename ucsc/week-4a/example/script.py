print("File Name: {}\nModule Name: {}".format( __file__, __name__))   # print __file__ and __name__

print("\nSymbol Table 1 {}\n{}:".format(__file__, dir())) # names in current scope 

import foobar

print("\nSymbol Table 2 {}\n{}:".format(__file__, dir())) # names in current scope after import of foobar

print("\nSymbol Table 3 {}\n{}:".format(__file__, dir(foobar))) # names in foobar

print()

foobar.foo()    # call functions in foobar.py as foobar.foo()

foobar.bar()
