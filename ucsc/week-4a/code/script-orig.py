
print("File Name: {} Module Name: {}".format(__file__, __name__))

print("\nSymbol Table 1: ", dir()) # dir() without arguments, return names in current scope

def foo():
    print("In foo")

print("\nSymbol Table 2: ", dir())  # names in current scope
 
def bar():
    print("In bar")

print("\nSymbol Table 3: ", dir())  # names in current scope

print("\nCalling foo() ...")
foo()

print("\nCalling bar() ...")
bar()
