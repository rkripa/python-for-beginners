print("From c.py,  __name__ = ", __name__)

def c():
    print("In c.py::c()")


# module test code under if below ...

# __name__ == "__main__", only when this module is executed  directly 
# __name__ == module_name when imported by other modules

if __name__ == "__main__":
    print("python3 c.py is being run")
    print("Calling c()")
    c()