# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:50:47 2019

@author: PAT
"""

from pydub.utils import mediainfo
from pydub import AudioSegment
import numpy as np
import acoustics.signal
import factorial

#files_path = 'D:/Pat/Germany Intern/music/'
#file_name = 'friendzone'
#file_type = '.mp3'
#fullfilename = files_path + file_name + file_type
#sound = AudioSegment.from_file(fullfilename) #also read file
## stereo signal to two mono signal for left and right channel
#split_sound = sound.split_to_mono()
#left_channel = np.array(split_sound[0].get_array_of_samples())
#right_channel = np.array(split_sound[1].get_array_of_samples())

fs = 250;
bw = 1/3;

fMin = 0.5;
fMax = 100;

octs = log2(fMax/fMin);
bmax = ceil(octs/bw);

fc = 39 # centre frequencies
fl = fc*2^(-bw/2); # lower cutoffs
fu = fc*2^(+bw/2); # upper cutoffs

numBands = length(fc);

b = cell(numBands,1);
a = cell(numBands,1);

figure
for nn in range(len(fc)):

    [b[nn],a[nn] = butter(2, [fl(nn) fu(nn)]/(fs/2), 'bandpass');
    [h,f]=freqz(b{nn},a{nn},1024,fs);

    hold on;
    plot(f, 20*log10(abs(h)) );

end
set(gca, 'XScale', 'log')
ylim([-50 0])