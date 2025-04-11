from pylab import*
import math as m
# np.arrange(m,n,p) array float da m a n-1, passo p non per forza intero
# np.linspace(i,k,n) float, equispaziati tra i e k inclusi, n come numero di intervallini
#gca().xaxis.set_major_locator(MaxNLocator(nbins=10))
ion()
x=arange(0,2*pi*10,0.1)
y_1=sin(x)
y_2=3*sin(x)
y_3=2*sin(0.5*x)
figure()
title("Sine functions")
xlabel("Time(sec)")
ylabel("Angle°")
plot(x,y_1,'r',label='sin(x)')
plot(x,y_2,'g',label='3*sin(x)')
plot(x,y_3,'b',label='2*sin(0.5*x)')
xlim(0,10)
ylim(-3,6)
legend(loc='upper right')
grid(True)
show()
