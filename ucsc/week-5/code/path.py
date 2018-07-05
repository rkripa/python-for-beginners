print("File Name: {} Module Name: {}".format( __file__, __name__))

import sys

print("Printing, sys.path  ...")
for dirpath in sys.path:
    print(dirpath)

