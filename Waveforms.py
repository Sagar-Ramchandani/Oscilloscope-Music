'''
The Waveform module, useful to generate specific waveforms in the XT mode
The waveforms use a single channel mode hence the same waveform is outputted on both
the left and right channels of the sound card
'''

import numpy as np
class Output:
	x=[]
	y=[]
	out=[]
	t=[]
def sine_wave(freq,phase=0,amplitude=1):
	t=np.arange(0,200*np.pi*freq/100, 0.001*freq/100*2*np.pi)
	out=np.sin(t+(phase*np.pi/180))*amplitude
	Output.t=t
	return out
def square(freq):
	out=sine_wave(freq)
	for i in range(0,len(out)):
		if out[i]>=0:
			out[i]=1
		elif out[i]<0:
			out[i]=-1
	return out
def sawtooth(freq):
	t=np.arange(0,2*np.pi*10,0.001*2*np.pi)
	out=[]
	for j in range(0,len(t)):
		a=0
		for i in range(1,50):
			a+=-1/(np.pi)/i*np.sin(2*np.pi*i*t[j]/625*freq) #Fourier series for Sawtooth wave
		out.append(a)
	max_out=max(out)
	for i in range(0,len(out)):
		out[i]=out[i]/max_out
	Output.t=t
	return out
def triangle(freq):
	out=[]
	t=np.arange(0,2*np.pi*10,0.001*2*np.pi*freq/150)
	for i in range(0,len(t)):
		a=0
		for n in range(1,40,2):
			a+=(-1)**((n-1)/2)/n**2*np.sin(n*np.pi*t[i]/2) #Fourier series for Triangle wave
		b=8/(np.pi**2)*a
		out.append(b)
	max_out=max(out)
	for i in range(0,len(out)):
		out[i]=out[i]/max_out
	Output.t=t
	return(out)
def exo_inc_sawtooth(freq):
	out=[]
	t=np.arange(0,2*np.pi*10,0.001*2*np.pi)
	a=0
	max_out=5
	for i in range(0,len(t)):
		if np.e**(t[i]-a)<=max_out:
			out.append(np.e**(t[i]-a))
		else:
			a=t[i]
			out.append(1)
	max_out=max(out)
	for i in range(0,len(out)):
		out[i]=((out[i]-1)/(max_out-1)-0.5)*2
	Output.t=t
	return out
def exo_dec_sawtooth(freq):
	f=freq/365
	t=np.arange(1,2*np.pi*10,0.001*2*np.pi*f)
	out=[]
	a=0
	max_out=1
	for i in range(0,len(t)):
		if np.log(t[i]-a)<=max_out:
			out.append(np.log(t[i]-a))
		else:
			a=t[i]-1
			out.append(0)
	for i in range(0,len(out)):
		out[i]=(out[i]-0.5)*2
	Output.t=t
	return out
def signal_periodic_maker(signal):
	position=len(signal)-1
	start=signal[0]
	diff=signal[1]-signal[0]
	if diff>=0:
		while position>0:
			if (abs(signal[position]-start)<0.01)and((signal[position]-signal[position-1])>0):
				break
			else:
				position-=1
	else:
		while position>0:
			if (abs(signal[position]-start)<0.01)and((signal[position]-signal[position-1])<0):
				break
			else:
				position-=1
	signal=signal[0:position]
	Output.t=Output.t[0:position]
	return (signal,position)