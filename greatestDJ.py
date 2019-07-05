# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:30:26 2019

@author: PAT
"""

# Import libraries
from pydub import AudioSegment
import librosa
import numpy as np
import matplotlib.pyplot as plt
from pydub.utils import get_array_type
import array
from scipy.io.wavfile import read
import soundfile as sf
import pyloudnorm as pyln
from crosscorrelation import pearson_def
from boxcounting2 import boxcounting
import csv
import os

def norm(arr):
    return arr/np.abs(arr).max()

def rms(segmentedAudio): 
    rms = segmentedAudio.rms
    if rms == 0:
        rms_dB = 20*np.log10(0.00001)
    else:
        rms_dB = 20*np.log10(rms)
    return rms_dB
    
def PPM(segmentedAudio):
#    peak_dBFS = segmentedAudio.max_dBFS
    if segmentedAudio.max == 0:
        peak_dB = 20*np.log10(0.00001)
    else:
        peak_dB = 20*np.log10(segmentedAudio.max)

#    if peak_dBFS = -inf: #below -1.796E308
    return peak_dB

def dynamicRange(segmentedAudio):
    ratio = abs(max(np.array(segmentedAudio.get_array_of_samples()))/min(np.array(segmentedAudio.get_array_of_samples())))
    if ratio == 0:
        ratio = 0.00001
    dr = abs(10 * np.log10(ratio))
#    print(max(np.array(segmentedAudio.get_array_of_samples())))
#    print(min(np.array(segmentedAudio.get_array_of_samples())))
    return dr

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

def panning(segmentedL, segmentedR):
    idx = segmentedR != 0
    if len(segmentedR[idx]) == 0:
        ratio = 1e9 # some big number
    else:
        ratio = np.average(segmentedL[idx] / segmentedR[idx])
    return rad_to_unit(ampradio_to_angle(ratio))

def segment(channel, file_name):
    total_time = len(channel) #Length of audio in msec
    no_segment = 4096
    segment_time = total_time/no_segment #in ms
    start = 0
    i = 0
    
    rmss = []
    peak_dB = []
    dr = []
    vu = []
    for i in range(no_segment):
        
        end = start + segment_time
        # extracting segment
        segmentedAudio = channel[start:end] #ms
#        print(min(np.array(segmentedAudio.get_array_of_samples())))
#        print("Done", chunk_name)
#        print('s',start)
#        print('e',end)
        start = end
        rmss.append(rms(segmentedAudio))
        peak_dB.append(PPM(segmentedAudio))
        dr.append(dynamicRange(segmentedAudio))
        # VU is loudness_dBFS
        vu.append(segmentedAudio.dBFS)
#    print(rmss)
#    print('vu', vu)
#    print(peak_dB)
#    print(peak_dBFS) #dBFS values are always less than or equal to zero
#    print(dr)
#    print('=====================================================')
    return zip(rmss, peak_dB, dr, vu)

def segment2(left_channel, right_channel, file_name):
    left_channel = np.array(left_channel.get_array_of_samples())
    right_channel = np.array(right_channel.get_array_of_samples())
    total_index = len(left_channel) #Length of audio in msec
    no_segment = 4096
    range_index = int(total_index/no_segment)
    start = 0
    count = 0
#    print(len(left_channel))
    pan = []
    xcor = []
    box = []
    for i in range(no_segment):
        end = start + range_index
        segmentedL = left_channel[start:end] #ms
        segmentedR = right_channel[start:end] #ms
        
        scale = 10
        scaleupL = np.round(norm(segmentedL) * scale, 1)
        scaleupR = np.round(norm(segmentedR) * scale, 1)
        
#        print('count',count)
#        print(panning(segmentedL, segmentedR))
#        print(pearson_def(segmentedL, segmentedR))
        print('segment no.' + str(i))
        pan.append(panning(segmentedL, segmentedR))
        xcor.append(pearson_def(segmentedL, segmentedR))
        box.append(boxcounting(scaleupL, scaleupR, scale))
#        box.append(boxcounting(left_channel, right_channel))
        start = end
        count += 1
            
    return zip(pan, xcor, box)

def main():
    files_path = 'D:/Pat/Germany Intern/Training/1. Martin Garrix/Amsterdam Music Festival (2014)/Wavepad MP3/'
    file_name = 'Alpharock - Pump This Party (Premiered by Martin Garrix)_179005305 - Spinnin Records'
    file_type = '.mp3'
    fullfilename = files_path + file_name + file_type
    sound = AudioSegment.from_file(fullfilename) #also read file
    # stereo signal to two mono signal for left and right channel
    split_sound = sound.split_to_mono()
    left_channel = split_sound[0]
    right_channel = split_sound[1]
    
    # rms, peak_dB, dr, vu
    fea_name1 = ['rms', 'peak_dB', 'dr', 'vu']
    print('start segmentL1')
    zippedL1 = segment(left_channel, file_name) # by time
    print('start segmentR1')
    zippedR1 = segment(right_channel, file_name)
    unzippedL = list(zip(*zippedL1))
    unzippedR = list(zip(*zippedR1))
    
    # write to individual csv
    for i in range(len(unzippedL)):
        dirname = 'dataset/' + file_name + '/' + 'Left' + '/'
        os.makedirs(dirname, exist_ok = True)
        with open(dirname + file_name + ' ' + str(fea_name1[i]) + '.csv', 'w', newline = '') as fp:
            a = csv.writer(fp, delimiter = ',')
            a.writerows(map(lambda x: [x], unzippedL[i]))
                
    for i in range(len(unzippedR)):
        dirname = 'dataset/' + file_name + '/' + 'Right' + '/'
        os.makedirs(dirname, exist_ok = True)
        with open(dirname + file_name + ' ' + str(fea_name1[i]) + '.csv', 'w', newline = '') as fp:
            a = csv.writer(fp, delimiter = ',')
            a.writerows(map(lambda x: [x], unzippedR[i]))
            
    # pan, xcor, box
    print('start segment2')
    fea_name2 = ['pan', 'xcor', 'box']
    zipped2 = segment2(left_channel, right_channel, file_name) # by array
    unzipped2 = list(zip(*zipped2))
    
    for i in range(len(unzipped2)):
        dirname = 'dataset/' + file_name + '/'
        os.makedirs(dirname, exist_ok = True)
        with open(dirname + file_name + ' ' + str(fea_name2[i]) + '.csv', 'w', newline = '') as fp:
            a = csv.writer(fp, delimiter = ',')
            a.writerows(map(lambda x: [x], unzipped2[i]))
    
if __name__== "__main__":
    main()
