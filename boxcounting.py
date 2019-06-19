# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:05:47 2019

@author: PAT
"""

import numpy as np
from pydub import AudioSegment

#
files_path = 'D:/Pat/Germany Intern/segmented2/'
file_name = 'hardwell84'
file_type = '.mp3'
fullfilename = files_path + file_name + file_type
sound = AudioSegment.from_file(fullfilename) #also read file
# stereo signal to two mono signal for left and right channel
split_sound = sound.split_to_mono()
left_channel = np.array(split_sound[0].get_array_of_samples())
right_channel = np.array(split_sound[1].get_array_of_samples())


#i =  0 # 3963
#while i < len(left_channel):
#    print(left_channel[i])
#    i += 1
def count_range_in_list(minY, channel):
    channel = np.array(channel.get_array_of_samples())
    diff = max(split_sound[0].get_array_of_samples()) - min(split_sound[0].get_array_of_samples())
    ratioX = len(split_sound[0])/20 #duration_in_milliseconds_per_small_area
    ratioY = (diff+1)/ 20
    startX = 0
    count = 0
    scale = [[],[]]
    for x in range(20):
        endX = startX + ratioX
        print('=====================================')
        print('startX',startX)
        print('endX',endX)
        print('----------------------')
        
        for i in range(len(split_sound[0])):
            if startX < i <= endX: 
                print('t',i)
                startY = minY
                for y in range(20):
                    endY = startY + ratioY
                    print('startY',startY)
                    for j in channel:
                            print('val',j)    
                    print('endY',endY)
                    startY = endY
        
        

            
        startX = endX
            
count_range_in_list(min(split_sound[0].get_array_of_samples()), split_sound[0])



'''    
def count_range_in_list(minY, channel):
    channel = np.array(channel.get_array_of_samples())
    channel.sort()
    diff = max(split_sound[0].get_array_of_samples()) - min(split_sound[0].get_array_of_samples())
    ratioX = len(split_sound[0])/20 #duration_in_milliseconds_per_small_area
    ratioY = (diff+1)/ 20
#    print(split_sound[0].max)
#    print(min(split_sound[0].get_array_of_samples()))
#    print(max(split_sound[0].get_array_of_samples()))
    
    num_value_per_scale = []
    startX = 0
    startY = minY
    for i in range(20):
        count = 0
        endX = startX + ratioX
        endY = startY + ratioY
#        print('startX',startX)
#        print('endX',endX)
        for x in range(len(split_sound[0])):
            if startX < x <= endX: 
                for y in channel:
                    if startY < y <= endY: 
#                        print('y',y)
                        count += 1
                break
        num_value_per_scale.append(count)
#        print('startY',startY)
#        print('endY',endY)
#        print('count',count)
        startY = endY
        startX = endX
#        print('==========')            
    return num_value_per_scale
print(count_range_in_list(min(split_sound[0].get_array_of_samples()), split_sound[0]))
'''

#def difference(a, b):
#    if (a == b):
#        return 0
#    elif (a > 0) and (b > 0):
#        return (abs(a - b))
#    elif (a > 0) and (b < 0):
#        return (abs(abs(b) - a))
#    elif (a < 0) and (b > 0):
#        return (abs(a) + b)
#    elif (a < 0) and (b < 0) and (a > b):
#        return abs(abs(a) - abs(b))
#    elif (a < 0) and (b < 0) and (a < b):
#        return abs(abs(b) - abs(a))
#
#        
#def count_range_in_list(segment):
##    
#    diff = difference(int(min(segment)), int(max(segment)))
#    ratioX = len(segment)/20 #duration_in_milliseconds_per_small_area
#    ratioY = (diff+1)/ 20
#    
#    num_value_per_scale = []
#    startX = 0
#    startY = int(min(segment))
#    for i in range(20):
#        count = 0
#        endX = startX + ratioX
#        endY = startY + ratioY
##        print('startX',startX)
##        print('endX',endX)
#        for x in range(len(segment)):
#            if startX < x <= endX: 
#                for y in segment:
#                    if startY < y <= endY: 
##                        print('y',y)
#                        count += 1
#                break
#        num_value_per_scale.append(count)
##        print('startY',startY)
##        print('endY',endY)
##        print('count',count)
#        startY = endY
#        startX = endX
##        print('==========')            
#    return max(num_value_per_scale)


#files_path = 'D:/Pat/Germany Intern/music/'
#file_name = 'Friendzone'
#file_type = '.mp3'
#fullfilename = files_path + file_name + file_type
#sound = AudioSegment.from_file(fullfilename) #also read file
## stereo signal to two mono signal for left and right channel
#split_sound = sound.split_to_mono()
#
#left_channel = split_sound[0]
#right_channel = split_sound[1]
#
#left_channel = np.array(left_channel.get_array_of_samples())
#right_channel = np.array(right_channel.get_array_of_samples())
#
#total_index = len(left_channel) #Length of audio in msec
#no_segment = 4096
#range_index = int(total_index/no_segment)
#start = 0
#count = 0
##    print(len(left_channel))
#
#for i in range(no_segment):
#    end = start + range_index
#    segmentedL = left_channel[start:end] #ms
#    segmentedR = right_channel[start:end] #ms
##    i =  2030 # 3963
##    while i < len(segmentedL):
##        print(segmentedL[i])
##        i += 1
##    break
##    print(np.array(segmentedL))
#    
#    
##    print('count',count)
##    print(panning(segmentedL, segmentedR))
##    print(pearson_def(segmentedL, segmentedR))
#    print(count_range_in_list(segmentedL))
#    break
#    start = end
#    count += 1


# =============================================================================
# 
# =============================================================================

#def count_range_in_list(minY, li):
#    startX = 0
#    for i in range(20):
#        endX = startX + ratioX
#        print('startX',startX)
#        print('endX',endX)
#            
#        for x in range(len(split_sound[0])):
#            ctr = 0
#            if startX < x <= endX: 
#                print('x',x)
#        startX = endX
#        print('==========')
#    
#    startY = minY
#    for i in range(20):
#        endY = startY + ratioY
#        print('startY',startY)
#        print('endY',endY)
#        for y in li:
#            if startY < y <= endY: 
#                print('y',y)
#        startY = endY
#        print('==========')
#            
#    return num_value_in_scale
            
#def count_range_in_list(minY, channel):
##    
#    diff = max(channel) - min(channel)
#    ratioX = len(channel)/20 #duration_in_milliseconds_per_small_area
#    ratioY = (diff+1)/ 20
##    print(split_sound[0].max)
##    print(min(split_sound[0].get_array_of_samples()))
##    print(max(split_sound[0].get_array_of_samples()))
#    
#    num_value_per_scale = []
#    startX = 0
#    startY = minY
#    for i in range(20):
#        count = 0
#        endX = startX + ratioX
#        endY = startY + ratioY
##        print('startX',startX)
##        print('endX',endX)
#        for x in range(len(split_sound[0])):
#            if startX < x <= endX: 
#                for y in channel:
#                    if startY < y <= endY: 
##                        print('y',y)
#                        count += 1
#                break
#        num_value_per_scale.append(count)
##        print('startY',startY)
##        print('endY',endY)
##        print('count',count)
#        startY = endY
#        startX = endX
##        print('==========')            
#    return num_value_per_scale
