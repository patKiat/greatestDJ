# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:40:52 2019

@author: PAT
"""
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import math

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
files_path = 'music/'
file_name = 'Friendzone1'
file_type = '.mp3'
fullfilename = files_path + file_name + file_type
sound = AudioSegment.from_file(fullfilename) #also read file
# stereo signal to two mono signal for left and right channel
split_sound = sound.split_to_mono()
left_channel = np.array(split_sound[0].get_array_of_samples())
right_channel = np.array(split_sound[1].get_array_of_samples())

#ratioX = difference(max(left_channel), min(left_channel))/20 
#ratioY = difference(max(right_channel), min(right_channel))/20

ratioX = 1822.2
ratioY = 1671.35

startX = min(left_channel)
scale = 20
count_per_scale = []
pair = removeDuplicates(list(zip(left_channel, right_channel)))
for x in range(scale):
    print('startX',startX)
    startY = min(right_channel)
    endX = startX + ratioX
    if x == (scale-1):
        endX = max(left_channel)
    print('endX',endX)
    for y in range(scale):
        print('-----------------------')
        print('startY',startY)
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

print('c',count)
print('pair', len(pair))
print('lmin',min(left_channel))
print('lmax',max(left_channel))
print('rmin',min(right_channel))
print('rmax',max(right_channel))
print('ratioX',ratioX)
print('ratioY',ratioY)
print(count_per_scale)
print(len(count_per_scale))

counti = 0
for i in count_per_scale:
    if(i > 0):
        counti += 1

print(counti)

#print(list(zip(left_channel, right_channel)))
#print(removeDuplicates(list(zip(left_channel, right_channel))))


#print(sound)

#for i in left_channel:
#    print(i)
    
#i =  0 # 3963
#while i < len(sound):
##    print(left_channel[i])
#    print(right_channel[i])
#    i += 1

#twod = np.column_stack((left_channel, right_channel))
#print(twod)
#left_channel = [-2,-2,-2,0,1,-2.6,6.3,6.5]
#right_channel = [-3.1,-3,-3,0,-1,-1.7,2.3,3]

#print(list(zip(left_channel, right_channel)))
#print([i for i in zip(left_channel, right_channel)])
#
#i = 0
#for l,r in zip(left_channel, right_channel):
#    print(l,r)
    
#    i +=1
#    if (i == 20):
#        break
#rng = np.random.RandomState(0)
#colors = rng.rand(2351)
#sizes = 3
#plt.scatter(left_channel, right_channel, c=colors, s=sizes, alpha=0.3, cmap='viridis')
#plt.title('Scatter plot pythonspot.com')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()