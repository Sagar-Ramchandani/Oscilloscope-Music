# Oscilloscope-Music

This Program is licensed under GPLv3

A set of tools to display images on an Oscilloscope using the sound card of the computer and XY mode of the Oscilloscope

Requirements- Python 3

Modules: 
matplotlib
numpy
pyaudio
PIL

Note: The pyaudio library may have trouble running on the newest versions of Python on Windows but is used in order to have
some amount of cross platform support.

Setup:

The repository is a project that is a proof of concept at being able to display images on an Oscilloscope
This is achieved by first connecting the two probes of the oscilloscope to the Audio out on the sound card of the computer
This is done to be able to probe the two channels of the audio output and the audio output required to generate an image is
made by the code

The set of tools contain the following

1. Waveform generator:
	This supports the generation of various waveforms on the Oscilloscope with frequency control
	These include Sine, Square, Sawtooth, Triangle and Beats
	And two custom waveforms Exponentially Decreasing Sawtooth and Exponentially increasing Sawtooth
	
	To access this on the Oscilloscope Music file, Select Channels to be 1

2. Lissajous Figures:
	This module allows the output of Lissajous figures in the XY mode with control on frequency and phase
	To access this on the Oscilloscope Music file, Select Channels to be 2
	
3. Spirograph:
	A mathematical function that can be plotted on the XY mode of the Oscilloscope,
	The Inner Radius parameter can be any positive value but is recommended to be kept small.
	The Radius ratio parameter can be any positive value but range of 0.1 to 1.5 is reccomended
	
	To access this on the Oscilloscope Music file, Select Channels to be 2
	
4. Pictures/Images:
	To output Pictures on the Oscilloscope. The Picture may be in Colour but will be Converted to Monochrome.
	
	The Picture has the following Requirements.
	1. The size of the image should ideally be a square and a power of two, say 64x64 or 128x128.
	2. The program has trouble displaying images of a higher resolution. This is because the Bandwidth of the Sound card
	becomes a limitation. Reccomended size is 64x64 or 128x128
	3. Formats of jpeg and png have been tested and are reccomended, but any format supported by PIL is expected to work
	
	Picture mode will convert your image into monochrome, and check if each indiviual pixel is in between the thresholds set.
	eg.
	0-black 255-white
	eg. if Lower Threshold =50 and Upper Threshold = 100
	Then all pixels between 50 and 100 are displayed.
	
	To access this on the Oscilloscope. Select Channels to be 2.
