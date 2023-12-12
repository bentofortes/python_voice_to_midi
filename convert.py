from scipy.io import wavfile
from scipy.fftpack import fft
import numpy as np
import sys


def main():
    audio_file = wavfile.read(sys.argv[1])
    sample_rate = audio_file[0]
    signal = np.array(audio_file[1])
    signal = signal[:, 0]

    ### Divisao em blocos

    blocks = []
    new = []
    

    # for i in signal:
        # if len(new) == sample_rate/20:
        #     blocks.append(np.array(new))
        #     new = []

        # else:
        #     new.append(i)~

    # start = 0
    # end = int(sample_rate/20)
    # while end < len(signal):
    #     blocks.append(signal[start: end])
    #     start += int(sample_rate/20)
    #     end += int(sample_rate/20)



    # result = []
    # for b in blocks:
    #     auto_corr = np.correlate(b, b, mode='full')
    #     auto_corr = auto_corr[int(len(auto_corr)/2) : ]
    #     peak = np.argmax(auto_corr[5:]) + 5 
    #     result.append(sample_rate/peak)

    auto_corr = np.correlate(signal, signal, mode='full')
    auto_corr = auto_corr[int(len(auto_corr)/2) : ]
    peak = np.argmax(auto_corr[5:]) + 5 
    # result.append(sample_rate/peak)
    print(sample_rate/peak)

    # print(result)


main()
