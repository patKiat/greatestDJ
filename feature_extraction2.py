# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:36:33 2019

@author: PAT
"""
from pydub import AudioSegment
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import numpy 
import matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import math
from pylab import*
from scipy.io import wavfile
samp_Freq, data_arr = wavfile.read('segmented/atb5.wav')

def rms(sampFreq, snd):
    snd = snd / (2.**15)
    #print(snd.shape)
    #print(snd.shape[0]/ sampFreq)
    s1 = snd[:,0] 
    s2 = snd[:,1] 
    timeArray = arange(0, snd.shape[0], 1)
    timeArray = timeArray / sampFreq
    timeArray = timeArray * 1000  #scale to milliseconds
    
    #plt.plot(timeArray, s1, color='k')
    #plt.ylabel('Amplitude')
    #plt.xlabel('Time (ms)')
    n = len(s1) 
    p = fft(s1) # take the fourier transform 
    nUniquePts = int(ceil((n+1)/2.0))
    p = p[0:nUniquePts]
    p = abs(p) #get the information about the magnitude of the frequency components
    p = p / float(n) # scale by the number of points so that
                     # the magnitude does not depend on the length 
                     # of the signal or on its sampling frequency  
    p = p**2  # square it to get the power 
    
    # odd nfft excludes Nyquist point
    if n % 2 > 0: # we've got odd number of points fft
        p[1:len(p)] = p[1:len(p)] * 2
    else:
        p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft
    
    freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);
    plt.subplot(2, 1, 1)
    plot(freqArray/1000, 10*log10(p), color='k')
    xlabel('Frequency (kHz)')
    ylabel('Power (dB)')
    rms_val = sqrt(mean(s1**2))
    print(rms_val)
    
    #plot(timeArray, s2, color='k')
    #ylabel('Amplitude')
    #xlabel('Time (ms)')
    n = len(s2) 
    p2 = fft(s2) # take the fourier transform 
    nUniquePts = int(ceil((n+1)/2.0))
    p2 = p[0:nUniquePts]
    p2 = abs(p2)
    p2 = p2 / float(n) # scale by the number of points so that
                     # the magnitude does not depend on the length 
                     # of the signal or on its sampling frequency  
    p2 = p2**2  # square it to get the power 
    
    # multiply by two (see technical document for details)
    # odd nfft excludes Nyquist point
    if n % 2 > 0: # we've got odd number of points fft
        p2[1:len(p2)] = p2[1:len(p2)] * 2
    else:
        p2[1:len(p2) -1] = p2[1:len(p2) - 1] * 2 # we've got even number of points fft
    
    freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);
    plt.subplot(2, 1, 2)
    plt.plot(freqArray/1000, 10*log10(p2), color='k')
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Power (dB)')
    rms_val2 = sqrt(mean(s2**2))
    print(rms_val2)

def main():
    rms(samp_Freq, data_arr)
  
if __name__== "__main__":
    main()
