'''
A highly experimental module with some basic functions that may allow for the
genertaion of images on the oscilloscope continously i.e creating a video.
The state of the module is highly experimental because it is severly limited by the
bandwidth the program consumes in the current state and what the sound card can offer
'''

import numpy as np
import array
import pyaudio
import time
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paFloat32, channels=2, rate= 200000, output=True)
class data:
	data=[]
def Recieve(samples):
	data.data.append(samples)
def play(file):
	samples=array.array('f', file).tostring()
	stream.write(samples)
def play_video():
	for samples in data.data:
		play(samples)