import numpy as np 
import wave
import struct
import matplotlib.pyplot as plt
import sys

usage = "usage : python3 sine_wave_filter.py file.wav [--l low_pass OR --h high_pass OR --b band_pass1 band_pass2] \
            l: Low_pass Hz value (int)\n \
        h: High pass Hz value (int)\n \
        b: Band pass Hz values (bottom top) (int)\n"

def args_parser(args):
    filters = {}
    file = ""
    j = 0
    for i, arg in enumerate(args):
        if arg.endswith(".wav"):
            file = arg
        elif "--" in arg:
            if i + 1 < len(args):
                try:      
                    if arg == "--l":
                        filters["l_" + str(j)] = int(args[i + 1])
                    elif arg == "--h":
                        filters["h_" + str(j)] = int(args[i + 1])
                    elif arg == "--b" and i + 2 < len(args):
                        filters["b_" + str(j)] = (int(args[i + 1], int(args[i + 2])))
                    j += 1
                except:
                    print("\nError with arg : ", arg + "\n", flush=True)
                    print(usage, flush=True)
                    exit(0)
            else:
                print("\nError with arg : ", arg + "\n", flush=True)
                print(usage, flush=True)
                exit(0)
    return (file, filters)

def read_file(file):
    return (sine_wave)

def get_freq(sine_wave):
    # Fast Fourier Transformations
    data_fft = np.fft.fft(sine_wave)
    # eliminate complex numbers
    frequencies = np.abs(data_fft)
    return (frequencies)

if __name__ == "__main__":
    file, filters = args_parser(sys.argv)
    print(file, filters)
##    sine_wave = read_file(file)
##    frequencies = get_freq(sine_wave):
##    if l != None:
##
##    elif h != None:
##
##    elif b != None:
        
