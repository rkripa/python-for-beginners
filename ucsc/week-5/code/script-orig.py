
print("File Name: {} Module Name: {}".format(__file__, __name__))

print("\nSymbol Table 1: ", dir())

def foo():
    print("In foo")

print("\nSymbol Table 2: ", dir())
def bar():
    print("In bar")

print("\nSymbol Table 3: ", dir())

print("\nCalling foo() ...")
foo()

print("\nCalling bar() ...")
bar()
