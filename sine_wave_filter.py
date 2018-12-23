import numpy as np 
import wave
import struct
import matplotlib.pyplot as plt
import sys, os

usage = "usage : python3 sine_wave_filter.py file.wav [--p] [--l low_pass OR --h high_pass OR --b band_pass1 band_pass2] [--r rate] [--t time] \n \
        p: Plot\n \
        l: Low_pass Hz value (int)\n \
        h: High pass Hz value (int)\n \
        b: Band pass Hz values (bottom top) (int)\n \
        r: sampling Rate (float)\n \
        t: Time of sample in seconds (float)\n "

def args_parser(args):
    filters = {}
    file = ""
    p = False
    r = 48000.0
    t = 1
    j = 0
    for i, arg in enumerate(args):
        if arg.endswith(".wav"):
            file = arg
        elif "--" in arg:
            if arg == "--p":
                p = True
            elif i + 1 < len(args):
                try:      
                    if arg == "--l":
                        filters["l_" + str(j)] = int(args[i + 1])
                    elif arg == "--h":
                        filters["h_" + str(j)] = int(args[i + 1])
                    elif arg == "--b" and i + 2 < len(args):
                        filters["b_" + str(j)] = (int(args[i + 1]), int(args[i + 2]))
                    elif arg == "--r":
                        r = float(args[i + 1])
                    elif arg == "--t":
                        t = float(args[i + 1])
                    j += 1
                except:
                    print("\nError with arg : ", arg + "\n", flush=True)
                    print(usage, flush=True)
                    exit(0)
            else:
                print("\nError with arg : ", arg + "\n", flush=True)
                print(usage, flush=True)
                exit(0)
    return (file, p, r, t, filters)

def read_file(file, r, t):
    frame_rate = r
    infile = "test.wav"
    num_samples = int(r * t)
    wav_file = wave.open(file, 'r')
    data = wav_file.readframes(num_samples)
    wav_file.close()
    data = struct.unpack('{n}h'.format(n=num_samples), data)
    sine_wave = np.array(data)
    return (sine_wave)

def get_freq(sine_wave):
    # Fast Fourier Transformations
    data_fft = np.fft.fft(sine_wave)
    # eliminate complex numbers
    frequencies = np.abs(data_fft)
    return (frequencies)

def apply_filter(frequencies, _filter, value):
    filtered_wave = []
    for idx, freq in enumerate(frequencies):
        if "l" in _filter:
            if idx < value:
                filtered_wave.append(frequencies[idx])
            else:
                filtered_wave.append(0)
        elif "h" in _filter:
            if idx > value:
                filtered_wave.append(frequencies[idx])
            else:
                filtered_wave.append(0)
        elif "b" in _filter:
            if idx > value[0] and idx < value[1]:
                filtered_wave.append(frequencies[idx])
            else:
                filtered_wave.append(0)
    filtered_wave = np.fft.ifft(filtered_wave)
    return filtered_wave

if __name__ == "__main__":
    file, p, r, t, filters = args_parser(sys.argv)
    if os.path.isfile(file):
        if len(filters) > 0:
            sine_wave = read_file(file, r, t)
            frequencies = get_freq(sine_wave)
            if p == True:
                plt.ion()
                plt.subplot(2 * len(filters) + 2,1,1)
                plt.title("Original sine wave")
                plt.plot(sine_wave)
                plt.subplot(2 * len(filters) + 2,1,2)
                plt.title("Frequencies")
                plt.plot(frequencies)
            i = 1
            filtered_wave = sine_wave
            for key, val in filters.items():
                filtered_wave = apply_filter(frequencies, key, val)
                frequencies = get_freq(filtered_wave)
                if p == True:
                    plt.subplot(2 * len(filters) + 2,1,2 + i)
                    plt.title("Filtered Audio Wave " + key)
                    plt.plot(filtered_wave)
                    plt.subplot(2 * len(filters) + 2,1,2 + i + 1)
                    plt.title("Filtered Audio Frequencies " + key)
                    plt.plot(frequencies)
                    i += 1
            if p == True:
                plt.show(block=True)
                
        else:
            print("\nError : no filter\n", flush=True)
            print(usage, flush=True)
            exit(0)
    else:
        print("\nError : file not found\n", flush=True)
        print(usage, flush=True)
        exit(0)
