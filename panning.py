# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:02:14 2019

@author: PAT
"""

import numpy as np
import scipy.io.wavfile as wavfile
from pydub import AudioSegment

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

files_path = 'D:/Pat/Germany Intern/music/'
file_name = 'hardwell'
file_type = '.wav'
fullfilename = files_path + file_name + file_type
sound = AudioSegment.from_file(fullfilename) #also read file
# stereo signal to two mono signal for left and right channel
split_sound = sound.split_to_mono()
left_channel = np.array(split_sound[0].get_array_of_samples())
right_channel = np.array(split_sound[1].get_array_of_samples())

idx = right_channel != 0
if len(right_channel[idx]) == 0:
    ratio = 1e9 # some big number
else:
    ratio = np.average(left_channel[idx] / right_channel[idx])

print(rad_to_unit(ampradio_to_angle(ratio)))