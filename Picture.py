'''
The module to handle Picture processing to convert to two arrays of X and Y co-ordinates

The image ideally needs to be in the size of a sqaure with the sidelength being a power
of two.
The way processing words is that the image is converted to Grayscale to simplify
processing, this converted 2D image is then scanned in the shape of a Hilbert Curve
of required order.

Scanning check the value of the image at the point and then if the value if in the
required thresold range between Upper and Lower Threshold, then the point is added to
a list of points to be drawn.

This approach is taken to ensure that points that are closer in the 2D space of the image
are close in the 1D array of points. This is a special property of Hilbert Curves and 
enables the creation of any monochrome image on the oscilloscope directly.

The drawback is that if the resolution is low i.e if the side of the image is small,
the display tends to create artifacts which show the Hilbert pattern of scanning,
a fix for this is to increase the side of the image but that is limited by the hardware
being used for this which is the sound card, as the sound card does not have enough
bandwidth for higher resolution images

'''
from PIL import Image
from Adders import assembler
from Hilbert import *
import numpy as np
import matplotlib.pyplot as plt
def Picture(path,threshold_up, threshold_down):
		img=Image.open(path).convert('LA').transpose(Image.FLIP_TOP_BOTTOM)
		data=np.asarray(img, dtype='int32')
		outx=[]
		outy=[]
		xi,xj=np.shape(data)[0],np.shape(data)[1]
		order=power_of_two(min(xi,xj))
		Hilbert(0.5,0.5,xi,0,0,xj,order) #Inital conditions
		Co_ords=Hilbert_return()
		for x,y in Co_ords:
			x=int(x)-1
			y=int(y)-1
			if (data[x][y][0]<threshold_up)and(data[x][y][0]>=threshold_down):
				outx.append(x)
				outy.append(y)
		'''
		Further code is included to Normalize the image so that it occupies the entire display
		'''
		max_x=max(outx)
		min_x=min(outx)
		max_y=max(outy)
		min_y=min(outy)
		for i in range(0,len(outx)):
				outx[i]=((outx[i]-min_x)/(max_x-min_x)-0.5)*2
		for i in range(0,len(outy)):
				outy[i]=((outy[i]-min_y)/(max_y-min_y)-0.5)*2
		out=assembler(outx,outy)
		plt.plot(outy,outx) #You may comment out the plot lines in order to directly display
		plt.show()
		return out
def power_of_two(number): #A single function to find find closest factor of two to the number that is <= the number
	count=0
	while number!=1:
		number=number//2
		count+=1
	return count