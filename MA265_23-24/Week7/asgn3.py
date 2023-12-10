from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x1, x2)
def f(x1, x2):
    return np.exp(x1 - x2)

# Generate data points
x1 = np.linspace(-2, 2, 100)
x2 = np.linspace(-2, 2, 100)

X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)

# Plot the function in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X1, X2, Z, cmap='coolwarm')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Z')
ax.set_title('f(x1, x2) = exp(x1 - x2)')
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()
