from pylab import * # I import all the neccesary libraries
from math import *
from scipy import *
# We write the Velocity Verlet algorithm, Euler and Euler-Cromer

def Pendulum_simulator(τ_1):

# Starting conditions:
#angles=[5,20,50,120,170]
#for angolo in angles:
    g=9.81
    l=1
    x_0=deg2rad(5)
    v_0=0.0
    τ=τ_1
    N=3000

    # Arrays:
    x_arr=zeros(N+1)
    v_arr=zeros(N+1)
    E_p_arr=zeros(N+1)
    E_k_arr=zeros(N+1)
    x_arr_E=zeros(N+1)
    v_arr_E=zeros(N+1)
    E_p_arr_E=zeros(N+1)
    E_k_arr_E=zeros(N+1)
    x_arr_V=zeros(N+1)
    v_arr_V=zeros(N+1)
    E_p_arr_V=zeros(N+1)
    E_k_arr_V=zeros(N+1)
    x_arr[0]=x_0
    v_arr[0]=v_0
    E_p_arr[0]=-cos(x_0)
    E_k_arr[0]=0.5*v_0**2
    x_arr_E[0]=x_0
    v_arr_E[0]=v_0
    E_p_arr_E[0]=-cos(x_0)
    E_k_arr_E[0]=0.5*v_0**2
    x_arr_V[0]=x_0
    v_arr_V[0]=v_0
    E_p_arr_V[0]=-cos(x_0)
    E_k_arr_V[0]=0.5*v_0**2

    # Acceleration: 
    a_0=(-g/l)*sin(x_0)

    # Euler:
    v_1=v_0+τ*a_0
    x_1=x_0+τ*v_0

    # Euler-Cromer:
    v_1=v_0+τ*a_0
    x_1=x_0+τ*v_1

    # Velocity Verlet:
    x_1=x_0+v_0*τ+0.5*a_0*τ**2
    a_1=(-g/l)*sin(x_1)
    v_1=v_0+0.5*τ*(a_0+a_1)

    '''# I start with the Euler-Cromer algorithm:
    for t_step in range(N):
        a_0=(-g/l)*sin(x_0)
        v_1=v_0+τ*a_0
        x_1=x_0+τ*v_1
        x_0=x_1
        v_0=v_1
        x_arr[t_step+1]=x_0
        v_arr[t_step+1]=v_0
        E_p_arr[t_step+1]=-cos(x_0)
        E_k_arr[t_step+1]=0.5*v_0**2'''

    # I continue with the Euler algorithm:
    '''for t_step in range(N):
        a_0=(-g/l)*sin(x_0)
        v_1_E=v_0+τ*a_0
        x_1_E=x_0+τ*v_0
        x_0=x_1_E
        v_0=v_1_E
        x_arr_E[t_step+1]=x_0
        v_arr_E[t_step+1]=v_0
        E_p_arr_E[t_step+1]=-cos(x_0)
        E_k_arr_E[t_step+1]=0.5*v_0**2'''

    # And I finish with the Velocity Verlet algorithm:
    for t_step in range(N):
        a_0=(-g/l)*sin(x_0)
        x_1_V=x_0+v_0*τ+0.5*a_0*τ**2
        a_1=(-g/l)*sin(x_1)
        v_1_V=v_0+0.5*τ*(a_0+a_1)
        x_0=x_1_V
        v_0=v_1_V
        x_arr_V[t_step+1]=x_0
        v_arr_V[t_step+1]=v_0
        E_p_arr_V[t_step+1]=-cos(x_0)
        E_k_arr_V[t_step+1]=0.5*v_0**2

    # I finally prepare the plot functions:

    time_arr=linspace(0,N*τ,N+1)
    '''plot(time_arr,x_arr,'blue')
    plot(time_arr,E_k_arr+E_p_arr,'cyan')
    plot(time_arr,x_arr_E,'red')
    plot(time_arr,E_k_arr_E+E_p_arr_E,'pink')'''
    plot(time_arr,x_arr_V,'yellow')
    plot(time_arr,E_k_arr_V+E_p_arr_V,'orange')
    grid(True)
    xlim(0,10)
    show()
    figure(2)
    '''plot(x_arr,v_arr,)
    plot(x_arr_E,v_arr_E,'blue')'''
    plot(x_arr_V,v_arr_V,'red')
    grid(True)
    show()


time=[0.001,0.01,0.1]
for τ_1 in time:
    Pendulum_simulator(τ_1)


