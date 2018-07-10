
print("File Name: {} Module Name: {}".format( __file__, __name__))

print("\nSymbol Table 1 {} {}:".format(__file__, dir())) # names in current scope
import foobar

print("\nSymbol Table 2 {} {}:".format(__file__, dir())) # names in current scope

print("\nSymbol Table 3 {} {}:".format(__file__, dir(foobar))) # names in foobar

foobar.foo()
foobar.bar()

