'''
Main file for interfacing with the program using the command line
Refer to README for Instructions on using the program using this interface

No plans for a GUI version at the moment
'''
from Waveforms import *
from Spirograph import *
from Adders import *
from Lissajous import Lissajous
from Picture import Picture
import numpy as np
import pyaudio
import array
import matplotlib.pyplot as plt
def main():
		channels=int(input("Channels? ")) #Selects if the plotting is in XT mode or XY
		if channels==1:
				print(" Waveform generator mode " )
				Waveform=int(input(" Select Waveform\n 1.Sine \n 2.Square \n 3.Sawtooth \n 4.Triangle \n 5.Exp Inc Sawtooth \n 6.Exp Dec Sawtooth \n 7.Beats \n"))
				frequency=int(input(" Frequency? "))
				Waveform_dict={1:sine_wave, 2:square, 3:sawtooth, 4:triangle, 5:exo_inc_sawtooth, 6:exo_dec_sawtooth}
				if Waveform in Waveform_dict:
						Output.out,a=signal_periodic_maker(Waveform_dict[Waveform](frequency))
						plt.plot(Output.t,Output.out) #Comment out the plt lines to stop graph plotting
						plt.show() 
						play(Output.out, 1)
				if Waveform==7:
						Frequency_Difference=int(input(" Frequency Difference "))
						Phase_Difference=int(input(" Phase Difference "))
						x=sine_wave(frequency)
						y=sine_wave(frequency+Frequency_Difference,Phase_Difference)
						play(adder(x,y),1,100000)
						
				else:
						print("Invalid option")
		elif channels==2:
				print(" XY mode ")
				Mode=int(input(" Select mode \n 1.Lissajous mode \n 2.Picture Mode \n 3.Spiroraph mode \n"))
				if Mode==1:
						Output.out=Lissajous(int(input('Freq X ')),int(input('Freq Y ')),float(input('Phase X ')),float(input('Phase Y ')))
						play(Output.out, 2)
				elif Mode==2:
						Output.out=Picture(input("Path for the image "), int(input("Upper Threshold ")), int(input("Upper Threshold ")))
						play(Output.out, 2, 100000)
				elif Mode==3:
						Output.out=spirograph(float(input("Inner Radius? ")), float(input("Radius ratio? ")))
						plt.show()
						play(Output.out, 2, 100000)
				else :
						print("Invalid option")
'''
The function play calls upon data to be played via the sound card
'''
def play(file,channel,Rate=100000):
		samples=array.array('f', file).tostring()
		p=pyaudio.PyAudio()
		stream=p.open(format=pyaudio.paFloat32, channels=channel, rate= Rate, output=True)
		while True:
			stream.write(samples)
if __name__ == "__main__":
		main()
