print("In main_3.py, from sound import *")

from sound import *   # see sound/__init__.py for __all__ 
                      # not recommended
                      # __all__ is commented out in sound/__init__.py,
                      # from sound import * will not work

print("In main_3.py, dir(): {}".format(dir()))
print("In main_3.py, dir(audio):{}".format(dir(audio)))
print("In main_3.py, calling audio.audio_func()")
audio.audio_func()
