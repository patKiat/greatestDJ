# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:07:51 2019

@author: PAT
"""

from pydub import AudioSegment
sound = AudioSegment.from_file('music/Friendzone.mp3')


halfway_point = len(sound) // 4096
first_half = sound[:halfway_point]

# create a new file "first_half.mp3":
first_half.export("music/Friendzone1.mp3", format="mp3")


