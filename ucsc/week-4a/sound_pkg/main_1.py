print("In main_1.py, import sound")

import sound   # importing a package does not include sub packages

print("In main_1.py, dir(): {} ".format(dir()))

print("In main_1.py, dir(sound): {} ".format(dir(sound)))

try:
    print("In main_1.py, calling sound.audio()")
    sound.audio()
except AttributeError:
    print("AttributeError, cant find sound.audio()")
