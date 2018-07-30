print("From a.py, __name__ = ", __name__)

print("From a.py, importing b")
import b

print("From a.py, calling b.b()")
b.b()

print("\nFrom a.py, Calling b.c.c()")
b.c.c()
