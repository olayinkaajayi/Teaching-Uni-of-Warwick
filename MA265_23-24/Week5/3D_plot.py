import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def objective(x, y):
    return 2 * x**2 + y**2

# Define the linear constraint
def constraint(x, y):
    return x + y - 1

# Create a meshgrid of points to plot
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)

# Evaluate the objective function and constraint at each point
z = objective(X, Y)
c = constraint(X, Y)

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, z, cmap='jet')
ax.contour(X, Y, c, colors='black')

# Mark the optimal value
ax.plot([1/3], [2/3], [objective(1/3, 2/3)], marker='o', markersize=10, color='red')

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title
ax.set_title('Objective Function and Linear Constraint')

# Show the plot
plt.show()
