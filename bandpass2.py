# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:09:14 2019

@author: PAT
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from crosscorrelation import pearson_def
from boxcounting2 import boxcounting
from pydub import AudioSegment

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
    
def third_octave(speech, channel):

    sampleRate = 44100.0
    nyquistRate = sampleRate/2.0
    
    #centerFrequency_Hz = np.array([39, 50, 63, 79, 99, 125, 157, 198, 250, 315, 397, 500, 630, 794, 1000, 1260, 1588, 2000, 2520, 3176, 4000, 5040, 6352, 8000, 10080, 12704, 16000, 20160, 2508, 32000])
    
    centerFrequency_Hz = np.array([39, 50, 63, 79, 99, 125, 157, 198, 250, 315, 397, 500, 630, 794, 1000, 1260, 1588, 2000, 2520, 3176, 4000, 5040, 6352, 8000, 10080, 12704, 16000])
    G = 2 #base-2 rules
    factor = np.power(G, 1.0/6.0)
    lowerCutoffFrequency_Hz=centerFrequency_Hz/factor;
    upperCutoffFrequency_Hz=centerFrequency_Hz*factor;
    
    #fig=plt.figure()
    #plt.title('Speech Signal')
    #plt.plot(speech)
    #plt.show()
    plt.figure()
    plt.ylabel('Magnitude [dB]')
    plt.xlabel('Frequency [rad/sample]')
    plt.title('Digital filter frequency response '+ channel)
    plt.grid()    
    
    for lower,upper in zip(lowerCutoffFrequency_Hz, upperCutoffFrequency_Hz):
        # Design filter
        sos = signal.butter( N=4, Wn=np.array([lower, upper])/nyquistRate, btype='bandpass', analog=False, output='sos');
    
        # Compute frequency response of the filter.
        w, h = signal.sosfreqz(sos)
        
#        for i in range(len(h)):
#            if h[i] == 0j:
#                h[i] = min(j for j in h if j > 0)
#                    
#        plt.plot(w, 20 * np.log10(abs(h)/max(h)), 'b')
        
        plt.plot(w, 20 * np.log10(abs(h)), 'b')
    
        # Filter signal
        filteredSpeech = signal.sosfiltfilt(sos, speech)
        
    plt.figure()
    plt.title('Third Octave-band Filtered Speech '+ channel)
    plt.plot(filteredSpeech)
    
    return filteredSpeech

#fs, speech = wavfile.read(filename='music/norm.wav');
#left_channel = speech[:, 0]
#right_channel = speech[:, 1]

files_path = 'D:/Pat/Germany Intern/music/'
file_name = '01-White-Noise-10min1'
file_type = '.mp3'
fullfilename = files_path + file_name + file_type
sound = AudioSegment.from_file(fullfilename) #also read file
# stereo signal to two mono signal for left and right channel
split_sound = sound.split_to_mono()
left_channel = split_sound[0]
right_channel = split_sound[1]
left_channel = np.array(left_channel.get_array_of_samples())
right_channel = np.array(right_channel.get_array_of_samples())

filteredSpeechL = third_octave(left_channel, 'L')
#filteredSpeechR = third_octave(right_channel, 'R')

#print('RMS for left channel', rms(filteredSpeechL))
#print('RMS for right channel', rms(filteredSpeechR))
#print('panning' , panning(filteredSpeechL, filteredSpeechR))
##boxcounting(filteredSpeechL, filteredSpeechR)
#print(pearson_def(filteredSpeechL, filteredSpeechR))

