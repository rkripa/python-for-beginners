print("From b.py, importing c")
import c

print("From b.py,  __name__ = ", __name__)

def b():
    print("In b.py::b()")
    print("From b.py::b(), calling c.c()")
    c.c()
