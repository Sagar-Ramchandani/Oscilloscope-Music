'''
File with functions to generate a Pseudo Hilbert Curve of nth order
'''

class co_ordinates:
	Hilbert_co_ords=[]
def Hilbert(x, y, xi, xj, yi, yj, n):
	#x and y are the coordinates of the bottom left corner
	#xi & xj are the i & j components of the unit x vector of the frame
	#similarly yi and yj
	if (n <= 0):
		co_ordinates.Hilbert_co_ords.append((x + (xi + yi)/2,y + (xj + yj)/2))
	else:
		Hilbert(x,           y,           yi/2, yj/2,  xi/2,  xj/2, n-1)
		Hilbert(x+xi/2,      y+xj/2 ,     xi/2, xj/2,  yi/2,  yj/2, n-1)
		Hilbert(x+xi/2+yi/2, y+xj/2+yj/2, xi/2, xj/2,  yi/2,  yj/2, n-1)
		Hilbert(x+xi/2+yi,   y+xj/2+yj,  -yi/2,-yj/2, -xi/2, -xj/2, n-1)
def Hilbert_return():
	return co_ordinates.Hilbert_co_ords
