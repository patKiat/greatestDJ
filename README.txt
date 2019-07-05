Requirement
1. Python version 3 up
2. Install ffmpeg (http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/)

Run
1. greatestDJ.py
   feature included:
	- rms() (Root mean square)
	- PPM() (Peak program meter)
	- dynamicRange()
	- panning() (call rad_to_unit and ampradio_to_angle function)
	- segment() (by time)
	- segment2() (by array)
	- main() (used to read stereo audio file and convert stereo(2 channels) to mono sound. There are 2 arrays for left and right channels)
	P.S. segment & segment2 used to split audio file into 4096 chunks then apply each feature to each chunk. There are 2 different segment function because it need to be applied with different libraries.

   call funtion in another python script crosscorrelation.py 

2. crosscorrelation.py is called by greatestDJ.py
3. boxcounting.py 
- You need to run separately.


	