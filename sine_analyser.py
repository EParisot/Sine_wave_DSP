import wave
import struct
import sys
import matplotlib.pyplot as plt
import sine_filter as SF
import numpy as np
from const import *

usage = "usage: python3 sine_analyser.py [.wav file]\n"

def args_parser(args):
    file = ""
    for arg in args:
        if arg.endswith(".wav"):
            file = arg
    return file

def read_file(file, r):
    infile = "test.wav"
    n_frames = int(r)
    wav_file = wave.open(file, 'r')
    data = wav_file.readframes(n_frames)
    wav_file.close()
    data = struct.unpack('{n}h'.format(n = n_frames), data)
    sine_wave = np.array(data)
    return (sine_wave)

def find_freq(frequencies):
    freq_dict = {}
    i = 1
    for idx, freq in enumerate(frequencies[:MAX_FREQ]):
        if freq > 1e8:
            freq_dict["b_" + str(i)] = (idx - 10, idx + 10)
            i += 1
    return freq_dict

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = args_parser(sys.argv[1:])
        if len(file) == 0:
            print("Error : File not found\n", usage)
            exit(0)
        sine_wave = read_file(file, R)
        # get Fourier transformation
        main_frequencies = SF.get_freq(sine_wave)
        filters = find_freq(main_frequencies)
        plt.ion()
        n_plots = 2 * len(filters) + 2
        plt.subplot(n_plots,1,1)
        plt.title("Original sine wave")
        plt.plot(sine_wave)
        plt.subplot(n_plots,1,2)
        plt.title("Frequencies")
        plt.plot(main_frequencies[:MAX_FREQ])
        i = 1
        for key, val in filters.items():
            # apply filters for found frequencies
            filtered_wave = SF.apply_filter(main_frequencies, key, val)
            frequencies = SF.get_freq(filtered_wave)
            plt.subplot(n_plots,1,2 + i)
            plt.title("Filtered Audio Wave " + key)
            plt.plot(filtered_wave)
            plt.subplot(n_plots,1,2 + i + 1)
            plt.title("Filtered Audio Frequencies " + key)
            plt.plot(frequencies[:MAX_FREQ])
            i += 2
        plt.show(block=True)
    else:
        print("Error : No file\n", usage)
        exit(0)
