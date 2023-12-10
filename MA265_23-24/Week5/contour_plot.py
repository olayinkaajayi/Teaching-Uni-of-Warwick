import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def objective(x, y):
  return 2*x**2 + y**2

# Define the constraint function
def constraint(x, y):
  return x + y - 1

# Create a grid of points to evaluate the objective function at
x = np.linspace(-1.5, 1.5, 100)
y = np.linspace(-1.5, 1.5, 100)

# Evaluate the objective function at the grid of points
z = np.zeros((len(x), len(y)))
for i in range(len(x)):
  for j in range(len(y)):
    z[i, j] = objective(x[i], y[j])

# Create a contour plot of the objective function
plt.contour(x, y, z, levels=10)

# Plot the constraint function
plt.plot([0, 1], [1, 0], 'k-')

# Add a red dot at the optimal value
plt.plot(1/3, 2/3, 'ro')

# Label the axes and plot title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour plot of objective function with optimal value')

# Show the plot
plt.show()
