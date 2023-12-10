import numpy as np
import matplotlib.pyplot as plt


d = np.linspace(0,180,1000)
x,y = np.meshgrid(d,d)
plt.imshow( ((x>=0) & (y>=0) & (6*y<=1200-9*x) & (12*y<=900-6*x) & (4.5*y<=675-7.5*x)).astype(int) ,
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);

x = np.linspace(0, 200, 2000)

# (9*x+6*y)<=1200
y2 = (1200-9*x)/6.0
# (6*x+12*y)<=900)
y3 = (900-6*x)/12.0
# (7.5*x+4.5*y)<=675
y4 = (675-7.5*x)/4.5

plt.plot(x, y2, label=r'$9x_1+6x_2\leq1200$')
plt.plot(x, y3, label=r'$6x_1+12x_2\leq900$')
plt.plot(x, y4, label=r'$7.5x_1+4.5x_2\leq675$')
plt.xlim(0,200)
plt.ylim(0,100)
plt.legend()#bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

plt.show()
