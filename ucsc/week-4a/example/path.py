print("File Name: {} Module Name: {}".format( __file__, __name__))

import sys

print("Printing, sys.path  ...")
for index, dirpath in enumerate(sys.path):
    print(index," : " ,dirpath)

