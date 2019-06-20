# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:25:01 2019

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


def segment(audioname, file_name):
    total_time = len(audioname) #Length of audio in msec
    no_segment = 4096
    segment_time = total_time/no_segment #in ms
    start = 0
    i = 0
    print(audioname)
    for i in range(no_segment):
        
        end = start + segment_time
        
        # Opening file and extracting segment
        
        segmentedAudio = audioname[start:end] #ms
        
        # Saving
        chunk_name = file_name +'{0}'.format(i)
    #    extract.export( 'segmented/'+file_name +'{0}.wav'.format(i), format=file_type)
        print("exporting", chunk_name)
        
        start = end
        rms(segmentedAudio)
    #    sound = extract.set_channels(1) # stereo to mono using pydub >> if nChannels == 2: np.mean(np.array([channels[0], channels[1]]), axis=0)
    #    samples = extract.get_array_of_samples()
    #    bit_depth = extract.sample_width * 8
    #    array_type = get_array_type(bit_depth)
    #    numeric_array = array.array(array_type, extract._data)
    #    print(numeric_array)
#        print(samples)
        
    print('=====================================================')

def rms(segmentedAudio):
    loudness = segmentedAudio.rms #compute dBFS. Loudness is logarithmic (rms is not), which makes dB a much more natural scale.
    print(loudness)
    
def main():
    files_path = 'D:/Pat/Germany Intern/music/'
    file_name = 'hardwell'
    file_type = '.wav'
    fullfilename = files_path + file_name + file_type
    rate, signal = read(fullfilename)
    # stereo signal to two mono signal for left and right channel
    channel1 = signal[:,0] # L
    channel2 = signal[:,1] # R
    myaudio1 = AudioSegment(
        channel1.tobytes(), 
        frame_rate=rate,
        sample_width=channel1.dtype.itemsize, 
        channels=1
    )
    myaudio2 = AudioSegment(
        channel2.tobytes(), 
        frame_rate=rate,
        sample_width=channel2.dtype.itemsize, 
        channels=2
    )
    segment(myaudio1, file_name)
    segment(myaudio2, file_name)
  
if __name__== "__main__":
    main()
