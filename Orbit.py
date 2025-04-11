from pylab import * # I import the necessary library
from matplotlib.animation import FuncAnimation, PillowWriter
# The labels must be 10^11 (Sun-Earth= 1.5*10^11 meters), and 10^7 (Years= 3.2*10^7 seconds)

# Starting conditions:
GM=4*pi**2
m=1/333000
x=0.98
y=0.0
v_x=0
v_y=2*pi
r=sqrt(x**2+y**2)
N_step=1000
τ=0.001

# Arrays:
x_arr=zeros(N_step+1)
y_arr=zeros(N_step+1)
v_x_arr=zeros(N_step+1)
v_y_arr=zeros(N_step+1)
θ_arr=zeros(N_step+1)
T_arr=zeros(N_step+1)
V_arr=zeros(N_step+1)
x_arr[0]=x
y_arr[0]=y
v_x_arr[0]=v_x
v_y_arr[0]=v_y
θ_arr[0]=arctan2(y,x)
T_arr[0]=0.5*m*(v_x**2+v_y**2)
V_arr[0]=-(GM*m)/r

# Velocity-Verlet:
for i_step in range(N_step):
    F_x=-GM*x/r**3
    F_y=-GM*y/r**3
    x+=v_x*τ+0.5*F_x*τ**2
    y+=v_y*τ+0.5*F_y*τ**2
    r=sqrt(x**2+y**2)
    F1_x=-GM*x/r**3
    F1_y=-GM*y/r**3
    v_x+=0.5*τ*(F_x+F1_x)
    v_y+=0.5*τ*(F_y+F1_y)
    x_arr[i_step+1]=x
    y_arr[i_step+1]=y
    v_x_arr[i_step+1]=v_x
    v_y_arr[i_step+1]=v_y
    θ_arr[i_step+1]=arctan2(y,x)
    T_arr[i_step+1]=0.5*m*(v_x**2+v_y**2)
    V_arr[i_step+1]=-(GM*m)/r

# I use the subplots functions to divide the three plots in one image
fig, axs=subplots(3,1,figsize=(8,10))
 
# Plot Orbit:
axs[0].set_xlabel("x (AU)") 
axs[0].set_ylabel("y (AU)") 
line_1,=axs[0].plot(x_arr,y_arr,'black',label='Earth')
axs[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
axs[0].axis("equal")
axs[0].grid(True)
axs[0].set_title("Earth orbit")
point_1,=axs[0].plot(x_arr,y_arr,'ro',markersize=4.5,label='Earth')

# Plot Angles:
t_arr=linspace(0,N_step*τ,N_step+1)
axs[1].set_xlabel('θ (rad)')
axs[1].set_ylabel('t (Y)')
line_2,=axs[1].plot(t_arr,θ_arr,'orange',label='Angles')
axs[1].grid(True)
axs[1].legend(loc='upper left', bbox_to_anchor=(1, 1))
axs[1].set_title("Angles")

# Plot Energy:
axs[2].set_xlabel('E (J)')
axs[2].set_ylabel('t (Y)')
line_3,=axs[2].plot(t_arr,T_arr,'red',label='Kinetic Energy')
line_4,=axs[2].plot(t_arr,V_arr,'blue',label='Potential Energy')
line_5,=axs[2].plot(t_arr,T_arr+V_arr,'green',label='Total Energy')
axs[2].grid(True)
axs[2].legend(loc='upper left', bbox_to_anchor=(1, 1))
axs[2].set_title("Energies")

# Now that I have the plots and single figure, I turn it into an animation
def init():
    line_1.set_data(x_arr,y_arr)
    line_2.set_data(t_arr,θ_arr)
    line_3.set_data(t_arr,T_arr)
    line_4.set_data(t_arr,V_arr)
    line_5.set_data(t_arr,T_arr+V_arr)
    point_1.set_data(x_arr,y_arr)
    return line_1,line_2,line_3,line_4,line_5,point_1


def update(frame):
    line_1.set_data(x_arr[:frame],y_arr[:frame])
    line_2.set_data(linspace(0,N_step*τ,frame),θ_arr[:frame])
    line_3.set_data(linspace(0,N_step*τ,frame),T_arr[:frame])
    line_4.set_data(linspace(0,N_step*τ,frame),V_arr[:frame])
    line_5.set_data(linspace(0,N_step*τ,frame),T_arr[:frame]+V_arr[:frame])
    point_1.set_data(x_arr[frame],y_arr[frame])
    return line_1,line_2,line_3,line_4,line_5,point_1


ani=FuncAnimation(fig,update,frames=N_step,init_func=init,blit=True,interval=0.05)
tight_layout()
show()
