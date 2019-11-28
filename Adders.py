'''
File with function for superimposition of waves or signals,

assembler for XY mode

adder for a XT mode
'''

'''
Assembler is designed to feed data into the PyAudio stream in 2 channel mode
The way this works is that the PyAudio play function takes in a single list and then
sends out all odd entries to one channel and even entries to another channel.
'''
def assembler(x,y):
		out=[]
		for i in range(0,len(x)):
				out.append(x[i])
				out.append(y[i])
		return out
def adder(x,y):
		out=[]
		for i in range(0,len(x)):
				out.append(x[i]+y[i])
		min_out=min(out)
		for i in range(0,len(out)):
				out[i]=out[i]-min_out #Removes the DC component of the output
		max_out=max(out)
		for i in range(0,len(out)):
				out[i]=(out[i]/max_out-0.5)*2 #Normalizes the output so it plays at max voltage
		return out