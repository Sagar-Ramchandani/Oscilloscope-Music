'''
The Spirograph Module that uses a numerical approach to solve for the position of
X and Y of the next co-ordinate for the display and then appends it to the list of points
to be drawn.
'''

import numpy as np
import matplotlib.pyplot as plt
from Adders import assembler
class General:
		Side_length=1
		Origin=(0,0)
class Outer:
		Origin=General.Origin
		radius=General.Side_length
class Inner:
		radius=General.Side_length*0.7
		Origin=(General.Origin[0]+Outer.radius-radius,
		General.Origin[1])
		Angle=0
		Angle_Speed=5
class Point:
		Rad_ratio=0.5
		Position=((Inner.Origin[0]+Inner.radius*Rad_ratio),
				  Inner.Origin[1])
		Angle=0
		Angle_Speed=-(Inner.Angle_Speed*Outer.radius/Inner.radius)
def circ_to_xy(radius,angle):
		x=(radius*np.cos(angle*np.pi/180))
		y=(radius*np.sin(angle*np.pi/180))
		return(x,y)
def update_inner():
		radius=Outer.radius-Inner.radius
		x,y=circ_to_xy(radius,Inner.Angle)
		Inner.Origin=((x+General.Side_length/2),
		(y+General.Side_length/2))
		Inner.Angle+=Inner.Angle_Speed
def update_point():
		radius=(Inner.radius*Point.Rad_ratio)
		x,y=circ_to_xy(radius,Point.Angle)
		x_prime,y_prime=Inner.Origin
		Point.Position=(x+x_prime,y+y_prime)
		Point.Angle+=Point.Angle_Speed
def spirograph(Inner_radius, Rad_ratio):
		x=[]
		y=[]
		Inner.radius=Inner_radius
		Point.Rad_ratio=Rad_ratio
		for i in range(0,1000):
				update_inner()
				update_point()
				x.append(Point.Position[0])
				y.append(Point.Position[1])
		min_x=min(x)
		min_y=min(y)
		for i in range(0,len(x)):
				x[i]=x[i]-min_x
				y[i]=y[i]-min_y
		max_x=max(x)
		max_y=max(y)
		for i in range(0,len(x)):
				x[i]=(x[i]/max_x-0.5)*2
				y[i]=(y[i]/max_y-0.5)*2
		plt.plot(x,y)
		out=assembler(x,y)
		return out