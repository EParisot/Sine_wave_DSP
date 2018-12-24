Sine Waves generator (multi-frequencies) and Sine waves filters (low-pass, high-pass, band-pass)

sine_wave.py:
usage : python3 sine_wave.py --f freq1 freq2 ... [--o out_file] [--a amp] [--t time]
        f: Frequencies in Hz (int, max 24000 Hz)
        o: Output file name (no extention) (string)
        a: Amplitude between 0 and 1 (float)
        t: Time of sample in seconds (float)

sine_wave_filter.py:
usage : python3 sine_filter.py file.wav [--l low_pass OR --h high_pass OR --b band_pass1 band_pass2] [...]
        l: Low_pass Hz value (int)
        h: High pass Hz value (int)
        b: Band pass Hz values (bottom top) (int)
