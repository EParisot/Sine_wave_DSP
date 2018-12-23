import numpy as np 
import wave
import struct
import matplotlib.pyplot as plt
import sys, os

usage = "usage : python3 sine_wave.py --f freq1 freq2 ... [--p] [--o out_file] [--r rate] [--a amp] [--t time]\n \
                    f: Frequencies in Hz (int)\n \
                    p: Plot wave (1000 first values)\n \
                    o: Output file name (no extention) (string)\n \
                    r: sampling Rate (float)\n \
                    a: Amplitude between 0 and 1 (float)\n \
                    t: Time of sample in seconds (float)\n "
                    

def args_parser(args):
    f = []
    p = False
    r = 48000.0
    a = 32767
    t = 1
    file_name = ""
    for i, arg in enumerate(args):
        if "--" in arg:
            if i + 1 < len(args):
                try:
                    if arg == "--f":
                        j = 0
                        while i + 1 + j < len(args) and "--" not in args[i + 1 + j]:
                            f.append(int(args[i + 1 + j]))
                            j += 1
                    elif arg == "--p":
                        p = True
                    elif arg == "--o":
                        file_name = args[i + 1]
                    elif arg == "--r":
                        r = float(args[i + 1])
                    elif arg == "--a":
                        a = float(args[i + 1]) * 32767
                    elif arg == "--t":
                        t = float(args[i + 1])
                except:
                    print("\nError with arg : ", arg + "\n", flush=True)
                    print(usage, flush=True)
                    exit(0)
            else:
                print("\nError with arg : ", arg + "\n", flush=True)
                print(usage, flush=True)
                exit(0)
    return(p, f, r, a, t, file_name)

def build_wave(f, r, a, t):
    print("\nBuilding wave...", flush=True)
    # calc sample size
    n_samples = int(r * t)
    # calc first sine wave
    sine_wave = np.array([(a / len(f)) * np.sin(2 * np.pi * f[0] * x / r) for x in range(n_samples)])
    # calc noises and add them to sine wave
    if len(f) > 1:
        for freq in f[1:]:
            sine_wave += np.array([(a / len(f)) * np.sin(2 * np.pi * freq * x / r) for x in range(n_samples)])
    print("Done", flush=True)
    return (sine_wave)

def write_wave(sine_wave, f, r, a, t, file_name):
    file = os.path.join("out/", file_name + ".wav")
    print("\nWriting sine wave in ", file, flush=True)
    n_samples = int(r * t)
    comptype = "NONE"
    compname = "not compressed"
    nchannels = 1
    sampwidth = 2
    # create file
    wav_file = wave.open(file, 'w')
    wav_file.setparams((nchannels, sampwidth, int(r), n_samples, comptype, compname))
    # write values in file
    for s in sine_wave:
       wav_file.writeframes(struct.pack('h', int(s)))
    print("Done", flush=True)

def get_freq(sine_wave):
    # Fast Fourier Transformations
    data_fft = np.fft.fft(sine_wave)
    # eliminate complex numbers
    frequencies = np.abs(data_fft)
    return (frequencies)

if __name__ == "__main__":
    p, f, r, a, t, file_name = args_parser(sys.argv)
    if len(f) > 0:
        sine_wave = build_wave(f, r, a, t)
        frequencies = get_freq(sine_wave)
    else:
        print("\nError: no frequencies\n",usage, flush=True)
        exit(0)
    if len(file_name) > 0:
        write_wave(sine_wave, f, r, a, t, file_name)
    if p == True:
        plt.ion()
        plt.subplot(2,1,1)
        plt.plot(sine_wave)
        plt.title("Audio Wave")
        plt.subplot(2,1,2)
        plt.plot([int(idx * (1 / t)) for idx, val in enumerate(frequencies)], frequencies)
        plt.title("Frequencies")
        plt.show(block=True)
