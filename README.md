# Sine Waves Generator (multi-frequencies), Player, filters (low-pass, high-pass, band-pass) and analyser (tones from spectrum)

## Installation:
```
pip(3) install -r requirements.txt
```

## Build wave (multiples frequencies allowed) sine_wave.py:
```
usage : python(3) sine_wave.py --f freq1 freq2 ... [--o out_file] [--a amp] [--t time]
        f: Frequencies in Hz (int, max 24000 Hz)
        o: Output file name (no extention) (string)
        a: Amplitude between 0 and 1 (float) (def 1)
        t: Time of sample in seconds (float) (def 1)
```

![](images/example1.bmp)

## Play wave from file or on Keyboard (whites : Q S D F G H J, blacks : Z E T Y U, 1s samples) sine_player.py:
```
usage: python(3) sine_player.py [wav_file]
(no file to play on keyboard)
```

## Apply filters to wave from file sine_filter.py:
```
usage : python(3) sine_filter.py file.wav [--l low_pass OR --h high_pass OR --b band_pass1 band_pass2] [...]
        l: Low_pass Hz value (int)
        h: High pass Hz value (int)
        b: Band pass Hz values (bottom top) (int)
```

![](images/example2.bmp)

## Find tones from spectrum sine_analiser.py:
```
usage: python(3) sine_analyser.py wav_file
```

![](images/example3.bmp)