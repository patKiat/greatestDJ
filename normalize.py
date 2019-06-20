# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:55:53 2019

@author: PAT
"""
import numpy as np
from pydub import AudioSegment

files_path = 'music/'
file_name = 'Friendzone1'
file_type = '.mp3'
fullfilename = files_path + file_name + file_type
sound = AudioSegment.from_file(fullfilename) #also read file
# stereo signal to two mono signal for left and right channel
split_sound = sound.split_to_mono()
left_channel = np.array(split_sound[0].get_array_of_samples())
right_channel = np.array(split_sound[1].get_array_of_samples())

norm_left_channel = []
norm_right_channel = []
#for x in range(len(left_channel)):
#    norm_val = [(1 * (left_channel[x] - min(left_channel)))/(max(left_channel) - min(left_channel))]
#    norm_left_channel.append(norm_val)
#print(norm_left_channel)

divider = max(left_channel) - min(left_channel)

a = left_channel-min(left_channel)
val = (a/divider)
for x in val:
    print(x)
#print(left_channel/divider)
