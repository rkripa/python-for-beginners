print("File Name: {} Module Name: {}".format( __file__, __name__))

import sys 
import os

print("\nPYTHONPATH environment variable: ", os.environ['PYTHONPATH'])

print("Printing, sys.path  ...")
for dirpath in sys.path:
    print(dirpath)

