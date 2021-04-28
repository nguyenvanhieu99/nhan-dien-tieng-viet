import librosa
import matplotlib.pyplot as plt
# a=librosa.get_duration(filename='record.wav')
# b=plt.
# print(a)
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

def draw_signal():
    audio_file = wave.open("record.wav", "r")

    # Extract Raw Audio from Wav File
    signal = audio_file.readframes(-1)
    signal = np.fromstring(signal, "Int16")


    # If Stereo
    if audio_file.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)

    plt.figure(2)
    plt.title("Signal Wave...")
    plt.plot(signal)
    plt.show()