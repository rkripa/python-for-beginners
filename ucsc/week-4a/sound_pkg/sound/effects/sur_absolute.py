print("In sound/effects/sur_absolute.py")

def surround():
    print("In sound/effects/sur_absolute.py::surround()")

    print("--------")
    print("In sound/effects/sur_absolute.py, **import sound.effects.echo as echo**")
    import sound.effects.echo as echo
    print("In sur_absolute.py, calling **echo.echo()**")
    echo.echo()

    print("--------")
    print("In sound/effects/sur_absolute.py, **from sound import audio**")
    from  sound import audio
    print("In sur_absolute.py, calling **audio.audio_func()**")
    audio.audio_func()

    print("--------")
    print("In sound/effects/sur_absolute.py, **from sound.filters import equalizer**")
    from sound.filters import equalizer
    print("In sur_absolute.py, calling **equalizer.equalizer()**")
    equalizer.equalizer()

    print("--------")
    print("In sound/effects/sur_absolute.py, **from sound.format.wave  import encode**")
    from sound.format.wave import encode
    print("In sur_absolute.py, calling **encode()**")
    encode()
