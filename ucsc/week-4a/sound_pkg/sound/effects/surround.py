print("In sound/effects/surround.py")

def surround():
    print("In sound/effects/surround.py::surround()")

    print("--------")
    print("In sound/effects/surround.py, **from . import echo**")
    from . import echo
    print("In surround.py, calling **echo.echo()**")
    echo.echo()

    print("--------")
    print("In sound/effects/surround.py, **from .. import audio**")
    from .. import audio
    print("In surround.py, calling **audio.audio_func()**)")
    audio.audio_func()

    print("--------")
    print("In sound/effects/surround.py, **from ..filters import equalizer**")
    from ..filters import equalizer
    print("In surround.py, calling **equalizer.equalizer()**")
    equalizer.equalizer()

    print("--------")
    print("In sound/effects/surround.py, **from ..format.wave  import encode**")
    from ..format.wave import encode
    print("In surround.py, calling **encode()**")
    encode()
