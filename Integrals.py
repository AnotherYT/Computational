from pylab import* # I import all the libraries I need for the two definitions for an integral: Trapezoid and Simpson
from scipy import*
from math import*
'''
N=100
x=linspace(0,2,N+1)
y=x**4-2*x+1
h=abs(x[1]-x[0])
# I define the integral with the trapezoid definition
trap=(0.5*h)*(y[0]+y[-1])
trap+=sum(y[1:-1])*h
# I define the same integral, using the Simpson definition
simp=(y[0]+y[-1])*(h/3)
simp+=(4*sum(y[1:-1:2])+2*sum(y[2:-1:2]))*(h/3)
print('Trapezoid solution=',trap,'\n','Simpson solution=',simp,'\n','Trapezoid error=',4.4-trap,'\n','Simpson error=',4.4-simp)
'''
exact=4.4
N_max=1800
trap_err=zeros((N_max-1)//2)
simp_err=zeros((N_max-1)//2)
i=0
for N in range(2,N_max,2):
    x=linspace(0,2,N+1)
    y=x**4-2*x+1
    h=abs(x[1]-x[0])
    trap=(0.5*h)*(y[0]+y[-1])
    trap+=sum(y[1:-1])*h
    
    simp=(y[0]+y[-1])*(h/3)
    simp+=(4*sum(y[1:-1:2])+2*sum(y[2:-1:2]))*(h/3)
    trap_err[i]=abs(trap-exact)
    simp_err[i]=abs(simp-exact)
    i=i+1
N_arr=range(2,N_max,2)
loglog(N_arr,trap_err,label='Trapezoid')
loglog(N_arr,simp_err,label='Simpson')
delta_Yt=log(trap_err[350])-log(trap_err[300])
delta_Ys=log(simp_err[350])-log(simp_err[300])
delta_X=log(N_arr[350])-log(N_arr[300])
slope_trap=delta_Yt/delta_X
slope_simp=delta_Ys/delta_X
print('Trapezoid solution=',trap,'\n','Simpson solution=',simp,'\n','Trapezoid slope=',slope_trap,'\n','Simpson slope=',slope_simp)
legend()
show()
