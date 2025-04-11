from pylab import * # I import all the libraries
from matplotlib.animation import FuncAnimation

# Starting conditions:
g=1
l=1
k=0.1
τ=0.01
N=30000
x_1=deg2rad(5)
x_2=deg2rad(0)
v_1=v_2=0.0

# Arrays:
x_1_arr=zeros(N+1)
x_2_arr=zeros(N+1)
v_1_arr=zeros(N+1)
v_2_arr=zeros(N+1)
T_arr=zeros(N+1)
V_arr=zeros(N+1)
E_arr=zeros(N+1)

x_1_arr[0]=x_1
x_2_arr[0]=x_2
v_1_arr[0]=v_1
v_2_arr[0]=v_2
T_arr[0]=0.5*(v_1**2+v_2**2)
V_arr[0]=g/l*(1-cos(x_1))+g/l*(1-cos(x_2))+0.5*k*(x_1-x_2)**2
E_arr[0]=T_arr[0]+V_arr[0]

# Starting forces:
a_1=(-g/l)*sin(x_1)-k*(x_1-x_2)
a_2=(-g/l)*sin(x_2)-k*(x_2-x_1)

# Velocity-Verlet:
for i_step in range(N):
    x_1n=x_1+v_1*τ+0.5*a_1*τ**2
    x_2n=x_2+v_2*τ+0.5*a_2*τ**2
    a_1n=(-g/l)*sin(x_1n)-k*(x_1n-x_2n)
    a_2n=(-g/l)*sin(x_2n)-k*(x_2n-x_1n)
    v_1n=v_1+0.5*τ*(a_1+a_1n)
    v_2n=v_2+0.5*τ*(a_2+a_2n)
    x_1=x_1n
    x_2=x_2n
    v_1=v_1n
    v_2=v_2n
    a_1=a_1n
    a_2=a_2n
    x_1_arr[i_step+1]=x_1
    x_2_arr[i_step+1]=x_2
    v_1_arr[i_step+1]=v_1
    v_2_arr[i_step+1]=v_2
    T_arr[i_step+1]=0.5*(v_1**2+v_2**2)
    V_arr[i_step+1]=g/l*(1-cos(x_1))+g/l*(1-cos(x_2))+0.5*k*(x_1-x_2)**2
    E_arr[i_step+1]=T_arr[i_step+1]+V_arr[i_step+1]

# Plotting:
t_arr=linspace(0,N*τ,N+1)
fig,axs=subplots(2,1,figsize=(10,10))

axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Angle (rad)')
line_1,=axs[0].plot(t_arr,x_1_arr,label='Pendulum 1')
line_2,=axs[0].plot(t_arr,x_2_arr,label='Pendulum 2')
axs[0].set_title('Double Pendulums')
axs[0].grid(True)
axs[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
'''
axs[1].set_xlabel('Angle (rad)')
axs[1].set_ylabel('Velocity (rad/s)')
axs[1].plot(x_1_arr,v_1_arr,'r',label='Pendulum 1')
axs[1].plot(x_2_arr,v_2_arr,'g',label='Pendulum 2')
axs[1].set_title('Angles to velocity')
axs[1].grid(True)
axs[1].legend(loc='upper left', bbox_to_anchor=(1, 1))
'''
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Energy (J)')
# axs[1].plot(t_arr,T_arr,'b',label='Kinetic Energy')
# axs[1].plot(t_arr,V_arr,'r',label='Potential Energy')
line_3,=axs[1].plot(t_arr,E_arr,'y',label='Total Energy')
axs[1].set_title('Energies')
axs[1].grid(True)
axs[1].legend(loc='upper left', bbox_to_anchor=(1, 1))

# Animation:
def init():
    line_1.set_data(t_arr,x_1_arr)
    line_2.set_data(t_arr,x_2_arr)
    line_3.set_data(t_arr,E_arr)
    return line_1,line_2,line_3


def update(frame):
    line_1.set_data(t_arr[:frame],x_1_arr[:frame])
    line_2.set_data(t_arr[:frame],x_2_arr[:frame])
    line_3.set_data(t_arr[:frame],E_arr[:frame])
    return line_1,line_2,line_3


ani=FuncAnimation(fig,update,frames=N,init_func=init,blit=True,interval=0.05)
tight_layout()
show()
