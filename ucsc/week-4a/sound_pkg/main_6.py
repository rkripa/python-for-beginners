print("In main_6.py, from sound.format import wave")
from sound.format import wave    # from package.subpackage import module 

print("In main_6.py, dir(): {}".format(dir()))
print("In main_6.py, calling wave.encode()")

wave.encode()
