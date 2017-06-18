#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import animation as animation
import math

#inicialização
class Pendulo:
	def __init__(self, m, l, x, v):
		self.m=m
		self.l=l
		self.x=x
		self.v=v
		self.w2= g/l
		self.T= 2*math.pi*math.sqrt(l/g)
		self.e= 0.5*self.m*(self.l*self.v)**2 +self.m*g*self.l*(1-math.cos(self.x))
#aceleração	
	def a(self, x, v, t):
		return -self.w2*math.sin(x) -gama*v +A*math.sin(wf*t)
#movimentação
	def move(self, t):
		at= self.a(self.x, self.v, t)
		self.x= self.x +self.v*dt +0.5*at*(dt**2)
		atem= self.a(self.x, self.v, t)
		vtem= self.v +0.5*(at+atem)*dt
		atem= self.a(self.x, vtem, t)
		self.v= self.v +0.5*(at+atem)*dt
		self.at= self.a(self.x, self.v, t)
		self.e= 0.5*self.m*(self.l*self.v)**2 +self.m*g*self.l*(1-math.cos(self.x))
#declaração das variáveis
g=9.8
gama=0.5
A=1.25
wf=2./3.
t=0.0
dt=0.2
#objeto
p1= Pendulo(1., 10., math.pi/6, 0)
#arrays
tmax=20*p1.T
t=np.arange(0, tmax, dt)

x=np.zeros(t.size)
v=np.zeros(t.size)
e=np.zeros(t.size)
x[0]=(p1.x+math.pi)%(2*math.pi)-math.pi
v[0]=p1.v
e[0]=p1.e


for i in range(t.size):
	p1.move(t[i])
	x[i]=(p1.x+math.pi)%(2*math.pi)-math.pi
	v[i]=p1.v
	e[i]=p1.e
	
#masterização dos gráficos
fig = plt.figure()
plt.title('Pendulo', fontsize=12)
#gráfico 1
XT=fig.add_subplot(331, xlim=(0, tmax), ylim=(min(x)*1.05, max(x)*1.05))
XT.xaxis.grid(False)
XT.yaxis.grid(False)
plt.setp(XT.get_xticklabels(), visible=False)
plt.xlabel('Tempo (s)')
plt.ylabel('Posicao (m)')
line1, = XT.plot([], [], 'g-', lw=1)
plt.legend(loc='upper right')
#gráfico 2
VT=fig.add_subplot(334, xlim=(0, tmax), ylim=(min(v)*1.05, max(v)*1.05))
VT.xaxis.grid(False)
VT.yaxis.grid(False)
plt.setp(VT.get_xticklabels(), visible=False)
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade(m/s)')
line2, = VT.plot([], [], 'y-', lw=1)
plt.legend(loc='upper right')
#gráfico 3
ET=fig.add_subplot(337, xlim=(0, tmax), ylim=(min(e)-0.005, max(e)+0.005))
ET.xaxis.grid(False)
ET.yaxis.grid(False)
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
line3, = ET.plot([], [], 'r-', lw=1)
plt.legend(loc='upper right')
#gráfico 4
VX=fig.add_subplot(122, xlim=(min(x)*1.05, max(x)*1.05), ylim=(min(v)*1.05, max(v)*1.05))
VX.xaxis.grid(True)
VX.yaxis.grid(True)
plt.xlabel('Posicao (m)')
plt.ylabel('Velocidade (m/s)')
line4, = VX.plot([], [], 'b.', lw=1)
plt.legend(loc='upper right')

#animação
def init():
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	line4.set_data([],[])
	return line1, line2, line3, line4,
	
def animate(i):
	tt= t[:i]
	xx= x[:i]
	vv= v[:i]
	ee= e[:i]
	line1.set_data(tt, xx)
	line2.set_data(tt, vv)
	line3.set_data(tt, ee)
	line4.set_data(xx, vv)
	return line1, line2, line3, line4,
		
anim=animation.FuncAnimation(fig, animate, init_func=init, frames=t.size,
interval=20, blit=True)

#anim.save('pendulo.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
