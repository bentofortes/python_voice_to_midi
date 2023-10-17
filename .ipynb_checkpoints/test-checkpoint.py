import sounddevice as sd
import numpy
import wave

duration = 1
fs = 44100
recording = sd.rec(duration * fs, samplerate = fs, channels = 1, dtype = 'float32')
sd.wait()