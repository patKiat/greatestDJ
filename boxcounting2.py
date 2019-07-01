# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:40:52 2019

@author: PAT
"""
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import math
from scipy.io import wavfile

def removeDuplicates(listofElements):
    
    # Create an empty list to store unique elements
    uniqueList = []
    
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList

def difference(a, b): # a > b
    if (a > 0) and (b > 0):
        return (abs(a - b))
    elif (a > 0) and (b < 0):
        return abs(a + abs(b))
    elif (a < 0) and (b < 0):
        return (abs(a) - abs(b))
   

#
files_path = ''
file_name = 'norm'
file_type = '.wav'
fullfilename = files_path + file_name + file_type

a, sound = wavfile.read("music/norm.wav")
sound = np.round(sound*20)
left_channel = sound[:,0]
right_channel = sound[:,1]
#for i in sound:
#    print(i)

#sound = AudioSegment.from_file(fullfilename) #also read file
## stereo signal to two mono signal for left and right channel
#split_sound = sound.split_to_mono()
#left_channel = np.array(split_sound[0].get_array_of_samples())
#right_channel = np.array(split_sound[1].get_array_of_samples())

ratioX = difference(max(left_channel), min(left_channel))/20 
ratioY = difference(max(right_channel), min(right_channel))/20

startX = min(left_channel)
scale = 20
count_per_scale = []
strX = []
strY =[]
pair = removeDuplicates(list(zip(left_channel, right_channel)))
for x in range(scale):
    print('startX',startX)
    strX.append(startX)
    startY = min(right_channel)
    endX = startX + ratioX
    if x == (scale-1):
        endX = max(left_channel)
    print('endX',endX)
    for y in range(5):
        print('-----------------------')
        print('startY',startY)
        strY.append(startY)
        endY = startY + ratioY
        if y == (scale-1):
            endY = max(right_channel)
        print('endY',endY)
        count = 0 # reset
        for l,r in pair:
            if (startX < l <= endX):
                if (startY < r <= endY):
                    print('0',l,r);
                    count+=1
                    print('count',count)
                elif (min(right_channel) == r and r == startY):
                    print('1',l,r);
                    count+=1
                    print('count',count)
            elif (min(left_channel) == l and l == startX):
                if (startY < r <= endY):
                    print('2',l,r)
                    count+=1
                    print('count',count)
                elif (min(right_channel) == r and r == startY):
                    print('3',l,r)
                    count+=1
                    print('count',count)
        count_per_scale.append(count)
        startY = endY
    startX = endX
    print('===============================')


#print('lmin',min(left_channel))
#print('lmax',max(left_channel))
#print('rmin',min(right_channel))
#print('rmax',max(right_channel))
#print('ratioX',ratioX)
#print('ratioY',ratioY)
#print(len(count_per_scale))
#print('pair', len(pair))
#print(sum(count_per_scale))

print(count_per_scale)
counti = 0
for i in count_per_scale:
    if(i > 0):
        counti += 1

print('No. of box that has value =', counti)


## Plot graph
rng = np.random.RandomState(0)
colors = rng.rand(2351)
sizes = 5
#plt.figure(figsize=(15,10))
plt.scatter(left_channel, right_channel, c=colors, s=sizes, alpha=1, cmap='viridis')
plt.title('Scatter plot channel')
plt.xlabel('L')
plt.ylabel('R')
plt.show()