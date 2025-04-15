'''
PDE → A*u_ぁぁ+2B*u_ぁぃ+C*u_ぃぃ+...=0, A^2+B^2+C^2=0, Parabolic: B^2-AC=0, Hellitic: B^2-AC<0, Hyperbolic: B^2-AC>0
I use the FTCS (forward-time-centered-space) → (Parabolic PDE)
T(x,t)=1/(sqrt(4*pi*k*t))*exp(-((x-x_0)^2)/(4kt)) → Heat diffusion
'''
from pylab import * # I import the libraries
from mpl_toolkits.mplot3d import axes3d

# Starting conditions:
N=100
t_step=1000
T=zeros((N,t_step))
T[50,0]=10
t_s=1
τ=0.3*t_s

# FTCS for loop:

for time in range (1,t_step):
    for i in range (1,N-1):
        T[i,time]=T[i,time-1]+0.5*τ/t_s*(T[i-1,time-1]+T[i+1,time-1]-2*T[i,time-1])

# 3D plot:
fig=figure()
ax=fig.add_subplot(111,projection='3d')
gridx,gridy=meshgrid(range(0,200),range(0,N,2))
ax.plot_wireframe(gridx,gridy,T[::2,0:200])
show()
