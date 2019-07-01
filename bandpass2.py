# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:09:14 2019

@author: PAT
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def rms(filteredSpeech):
    rms = np.sqrt(np.mean(np.power(filteredSpeech, 2)))
    rms_db = 20*np.log10(rms)
    return rms_db

# https://stackoverflow.com/questions/35543986/python-get-audio-pan-l-r
def ampradio_to_angle(x):
    """ converts ratio of amplitude of left and right channel to degree in radians """
    if x == 1:
        return 0
    else:
        return 2 * np.arctan((-1 * np.sqrt(2) * np.sqrt(x*x + 1) + x + 1) / (x - 1))

def rad_to_unit(x):
    """ scales -45° to 45° in radiants between -1 and 1 """
    return np.degrees(x)/45

def panning(filteredSpeechL, filteredSpeechR):
    idx = filteredSpeechR != 0
    if len(filteredSpeechR[idx]) == 0:
        ratio = 1e9 # some big number
    else:
        ratio = np.average(filteredSpeechL[idx] / filteredSpeechR[idx])
    return rad_to_unit(ampradio_to_angle(ratio))

sampleRate = 44100.0
nyquistRate = sampleRate/2.0

#centerFrequency_Hz = np.array([39, 50, 63, 79, 99, 125, 157, 198, 250, 315, 397, 500, 630, 794, 1000, 1260, 1588, 2000, 2520, 3176, 4000, 5040, 6352, 8000, 10080, 12704, 16000, 20160, 2508, 32000])

centerFrequency_Hz = np.array([39, 50, 63, 79, 99, 125, 157, 198, 250, 315, 397, 500, 630, 794, 1000, 1260, 1588, 2000, 2520, 3176, 4000, 5040, 6352, 8000, 10080, 12704, 16000])
G = 2 #base-2 rules
factor = np.power(G, 1.0/6.0)
lowerCutoffFrequency_Hz=centerFrequency_Hz/factor;
upperCutoffFrequency_Hz=centerFrequency_Hz*factor;

fs, speech = wavfile.read(filename='music/norm.wav');
left_channel = speech[:, 0]
right_channel = speech[:, 1]
fig=plt.figure()
#plt.title('Speech Signal')
#plt.plot(speech)
#plt.show()
plt.ylabel('Amplitude [dB]')
plt.xlabel('Frequency [rad/sample]')
plt.title('Digital filter frequency response')
plt.grid()    

for lower,upper in zip(lowerCutoffFrequency_Hz, upperCutoffFrequency_Hz):
    # Design filter
    sos = signal.butter( N=4, Wn=np.array([lower, upper])/nyquistRate, btype='bandpass', analog=False, output='sos');

    # Compute frequency response of the filter.
    w, h = signal.sosfreqz(sos)
    
    plt.plot(w, 20 * np.log10(abs(h)), 'b')

    # Filter signal
    filteredSpeechL = signal.sosfiltfilt(sos, left_channel)
    filteredSpeechR = signal.sosfiltfilt(sos, right_channel)
    
fig=plt.figure()
plt.title('Third Octave-band Filtered Speech L')
plt.plot(filteredSpeechL)
fig=plt.figure()
plt.title('Third Octave-band Filtered Speech R')
plt.plot(filteredSpeechR)

print('RMS for left channel', rms(filteredSpeechL))
print('RMS for right channel', rms(filteredSpeechR))
print('panning' , panning(filteredSpeechL, filteredSpeechR))

