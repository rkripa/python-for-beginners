print("File Name: {} Module Name: {}".format( __file__, __name__))

import sys 
import os

print("\nPYTHONPATH environment variable: ", os.environ['PYTHONPATH'])

print("Printing, sys.path  ...")
for index, dirpath in enumerate(sys.path):
    print(index, " : ", dirpath)

