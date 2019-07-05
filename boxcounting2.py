# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:40:52 2019

@author: PAT
"""
#import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
#from scipy.io import wavfile
from collections import OrderedDict 

def difference(a, b): # a > b
    if (a > 0) and (b > 0):
        return (abs(a - b))
    elif (a > 0) and (b < 0):
        return abs(a + abs(b))
    elif (a < 0) and (b < 0):
        return (abs(a) - abs(b))

def boxcounting(left_channel, right_channel, scale):
    ratioX = difference(max(left_channel), min(left_channel))/scale
    ratioY = difference(max(right_channel), min(right_channel))/scale
    startX = min(left_channel)
#    count_per_scale = []
    countbox = 0
    pair = list(OrderedDict.fromkeys(list(zip(left_channel, right_channel)))) 

    for x in range(scale):
#        print('startX',startX)
        startY = min(right_channel)
        endX = startX + ratioX
        if x == (scale-1):
            endX = max(left_channel)
#        print('endX',endX)
        for y in range(scale):
#            print('-----------------------')
#            print('startY',startY)
            endY = startY + ratioY
            if y == (scale-1):
                endY = max(right_channel)
#            print('endY',endY)
            count = 0 # reset
            for l,r in pair:
                if (startX < l <= endX):
                    if (startY < r <= endY):
                        count+=1
#                        print('0',l,r)
#                        print('count',count)
                    elif (min(right_channel) == r and r == startY):
                        count+=1
#                        print('1',l,r)
#                        print('count',count)
                elif (min(left_channel) == l and l == startX):
                    if (startY < r <= endY):
                        count+=1
#                        print('2',l,r)
#                        print('count',count)
                    elif (min(right_channel) == r and r == startY):
                        count+=1
#                        print('3',l,r)
#                        print('count',count)
#            count_per_scale.append(count)
            if count != 0:
                countbox += 1
            startY = endY
        startX = endX
#        print('===============================')
    
#    
#    print(count_per_scale)
#    countbox = 0
#    for i in count_per_scale:
#        if(i > 0):
#            countbox += 1
#    countbox = np.count_nonzero(count_per_scale)
#    print('No. of box that has value =', countbox)
    return countbox

#files_path = 'D:/Pat/Germany Intern/Training/1. Martin Garrix/Amsterdam Music Festival (2014)/Wavepad MP3/'
#file_name = 'Alpharock - Pump This Party (Premiered by Martin Garrix)_179005305 - Spinnin Records'
#file_type = '.mp3'
#fullfilename = files_path + file_name + file_type
#sound = AudioSegment.from_file(fullfilename) #also read file
##sound = np.round(sound*20)
## stereo signal to two mono signal for left and right channel
#split_sound = sound.split_to_mono()
#left_channel = np.array(split_sound[0].get_array_of_samples())
#right_channel = np.array(split_sound[1].get_array_of_samples())
##norm and scale up
#scale = 10
#scaleupL = np.round((left_channel/np.abs(left_channel).max())* scale,1) 
#scaleupR = np.round((right_channel/np.abs(right_channel).max())* scale,1) 
#
#print('start count')
#boxcounting(scaleupL, scaleupR, scale)
