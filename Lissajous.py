'''
Lissajous module is to be imported to be able to generate Lissajous figures using the
XY mode of the oscilloscope, These figures are based on just the perpendicular
superposition of the sine waves of suitable frequency and voltage

This mode is included in order for the project to also be used as a demonstration tool
for the XY mode of an oscilloscope
'''

from Waveforms import sine_wave
from Adders import assembler
import matplotlib.pyplot as plt
from Video import *
def Lissajous(freq_x, freq_y, phase_x, phase_y):
	x=sine_wave(freq_x,phase_x)
	y=sine_wave(freq_y,phase_y)
	out=assembler(x,y)
	plt.plot(x,y)
	plt.show()
	return out

'''
Lissajous_phase_changing is an experimental mode that attempts to use the Video Module
in order to display a series of Phase changing lissajous figures
The experimental part is because the current code does all the proccessing for the
generation of the Lissajous pattern before actually displaying any output
thus it cannot be used to generate longer clips or clips where the rate of phase change
or the step in phase of the figures is small as the proccessing will cause the program
to not display any output for a while
'''
def Lissajous_phase_changing(freq_x, freq_y, phase_difference, rate_change_phase):
	n_samples=int(180/rate_change_phase)
	while n_samples>1:
		x=sine_wave(freq_x,0)
		y=sine_wave(freq_y,phase_difference)
		out=assembler(x,y)
		Recieve(out)
		phase_difference+=rate_change_phase
		n_samples-=1
		plt.plot(x,y)
		plt.show()
	play_video()
