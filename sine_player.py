import pyaudio  
import wave
from pynput.keyboard import Key, Listener, KeyCode
import sys
import sine_wave as SW
import numpy as np
from const import *

usage = "usage: python3 sine_player.py [.wav file]\n"

def args_parser(args):
    file = ""
    for arg in args:
        if arg.endswith(".wav"):
            file = arg
    return file

def read_file(file):
    #define stream chunk   
    chunk = 1024  
    #open a wav format music  
    f = wave.open(file, "rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    f_stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    #read data  
    data = f.readframes(chunk)  
    #play stream  
    while data:  
        f_stream.write(data)  
        data = f.readframes(chunk)  
    #stop stream  
    f_stream.stop_stream()  
    f_stream.close()  
    #close PyAudio  
    p.terminate()

freqs = []
def play_wave(f):
    sine_wave = SW.build_wave(f, R, 1, 1).astype(np.float32)
    # play. May repeat with different volume values (if done interactively) 
    stream.write(sine_wave)

def on_press(key):
    freq_len = len(freqs)
    if key == Key.esc:
        # Stop listener
        return False
    elif key == KeyCode(char='q') and NOTES['C4'] not in freqs:
        freqs.append(NOTES['C4'])
    elif key == KeyCode(char='z') and NOTES['Db4'] not in freqs:
        freqs.append(NOTES['Db4'])
    elif key == KeyCode(char='s') and NOTES['D4'] not in freqs:
        freqs.append(NOTES['D4'])
    elif key == KeyCode(char='e') and NOTES['Eb4'] not in freqs:
        freqs.append(NOTES['Eb4'])
    elif key == KeyCode(char='d') and NOTES['E4'] not in freqs:
        freqs.append(NOTES['E4'])
    elif key == KeyCode(char='f') and NOTES['F4'] not in freqs:
        freqs.append(NOTES['F4'])
    elif key == KeyCode(char='t') and NOTES['Gb4'] not in freqs:
        freqs.append(NOTES['Gb4'])
    elif key == KeyCode(char='g') and NOTES['G4'] not in freqs:
        freqs.append(NOTES['G4'])
    elif key == KeyCode(char='y') and NOTES['Ab4'] not in freqs:
        freqs.append(NOTES['Ab4'])
    elif key == KeyCode(char='h') and NOTES['A4'] not in freqs:
        freqs.append(NOTES['A4'])
    elif key == KeyCode(char='u') and NOTES['Bb4'] not in freqs:
        freqs.append(NOTES['Bb4'])
    elif key == KeyCode(char='j') and NOTES['B4'] not in freqs:
        freqs.append(NOTES['B4'])
    if len(freqs) > 0 and len(freqs) != freq_len:
        play_wave(freqs)

def on_release(key):
    freq_len = len(freqs)
    if key == KeyCode(char='q') and NOTES['C4'] in freqs:
        freqs.remove(NOTES['C4'])
    elif key == KeyCode(char='z') and NOTES['Db4'] in freqs:
        freqs.remove(NOTES['Db4'])
    elif key == KeyCode(char='s') and NOTES['D4'] in freqs:
        freqs.remove(NOTES['D4'])
    elif key == KeyCode(char='e') and NOTES['Eb4'] in freqs:
        freqs.remove(NOTES['Eb4'])
    elif key == KeyCode(char='d') and NOTES['E4'] in freqs:
        freqs.remove(NOTES['E4'])
    elif key == KeyCode(char='f') and NOTES['F4'] in freqs:
        freqs.remove(NOTES['F4'])
    elif key == KeyCode(char='t') and NOTES['Gb4'] in freqs:
        freqs.remove(NOTES['Gb4'])
    elif key == KeyCode(char='g') and NOTES['G4'] in freqs:
        freqs.remove(NOTES['G4'])
    elif key == KeyCode(char='y') and NOTES['Ab4'] in freqs:
        freqs.remove(NOTES['Ab4'])
    elif key == KeyCode(char='h') and NOTES['A4'] in freqs:
        freqs.remove(NOTES['A4'])
    elif key == KeyCode(char='u') and NOTES['Bb4'] in freqs:
        freqs.remove(NOTES['Bb4'])
    elif key == KeyCode(char='j') and NOTES['B4'] in freqs:
        freqs.remove(NOTES['B4'])

def key_listener():
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release,
            suppress=True) as listener:
        listener.join()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = args_parser(sys.argv[1:])
        if len(file) == 0:
            print("Error : File not found\n", usage)
            exit(0)
        read_file(file)
    else:
        p = pyaudio.PyAudio()
        global stream
        stream = p.open(format = pyaudio.paFloat32,  
                    channels = 1,
                    rate=R,
                    output=True)
        key_listener()
        stream.stop_stream()
        stream.close()
        p.terminate()
