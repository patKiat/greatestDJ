# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:58:40 2019

@author: PAT
"""


# https://github.com/jiaaro/pydub

from pydub import AudioSegment
#AudioSegment.converter = "D:/Pat/Germany Intern/ffmpeg/bin/ffmpeg.exe"
#AudioSegment.ffmpeg = "D:/Pat/Germany Intern/ffmpeg/bin/ffmpeg.exe"
#AudioSegment.ffprobe ="D:/Pat/Germany Intern/ffmpeg/bin/ffprobe.exe"
#song = AudioSegment.from_mp3('hardwell.mp3')




#files_path = 'D:/Pat/Germany Intern/'
#file_name = 'hardwell'
#
#
#startMin = 0
#startSec = 0
#
#endMin = 1
#endSec = 0
#
## Time to miliseconds
#startTime = startMin*60*1000+startSec*1000
#endTime = endMin*60*1000+endSec*1000
#
## Opening file and extracting segment
#song = AudioSegment.from_mp3( files_path+file_name+'.mp3' )
#extract = song[startTime:endTime]
#
## Saving
#extract.export( 'segmented/'+file_name+'-extract.mp3', format="mp3")



from pydub import AudioSegment
#from pydub.utils import mediainfo
from pydub.utils import make_chunks
import math

#myaudio = AudioSegment.from_file("hardwell.mp3" , "mp3")

files_path = 'D:/Pat/Germany Intern/music/'
file_name = 'hardwell'
total_time = len(myaudio) #Length of audio in msec
no_segment = 4096
segment_time = total_time/no_segment #in ms
start = 0
i = 0

for i in range(no_segment):
    
    end = start + segment_time
    
    # Opening file and extracting segment
    song = AudioSegment.from_mp3(files_path+file_name+'.mp3' )
    extract = song[start:end] #ms
    
    # Saving
    chunk_name = file_name +'{0}.mp3'.format(i)
    extract.export( 'segmented/'+file_name +'{0}.mp3'.format(i), format="mp3")
    print("exporting", chunk_name)
    
    start = end
    