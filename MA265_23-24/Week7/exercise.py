import numpy as np
from itertools import product
import matplotlib.pyplot as plt


step_size = 1
points = np.arange(0, 5, step_size)

def determinant_Vandermonde(points):
    """Computes the determinant of a vandermonde matrix given the pair of points"""
    all_pairs = product(points, points)
    pairs = [a-b for a,b in all_pairs]
    det = np.product(pairs)

    return det


plt.scatter(points,[1]*len(points))
