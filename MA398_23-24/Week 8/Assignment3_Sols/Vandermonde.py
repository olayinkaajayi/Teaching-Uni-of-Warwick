#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:36:32 2023

@author: herzallr
"""


import numpy as np
import matplotlib.pyplot as plt

def Vandermonde(x, d):
    """Create a Vandermonde matrix for given x and degree d."""
    n = len(x)
    V = np.zeros((n, d + 1))
    for i in range(n):
        for j in range(d + 1):
            V[i, j] = x[i]**j
    return V

# Generate equidistant points in [-1, 1]
n_values = range(2, 101)  # Example range for n values
condition_numbers = []

for n in n_values:
    x = np.linspace(-1, 1, n)
    V = Vandermonde(x, n - 1)
    cond_num = np.linalg.cond(V, p=2)  # Calculate condition number in 2-norm
    condition_numbers.append(cond_num)

# Plotting the condition numbers
plt.plot(n_values, condition_numbers)
plt.yscale('log')  # Log scale as condition numbers can vary widely
plt.xlabel('n (size of matrix)')
plt.ylabel('Condition Number')
plt.title('Condition Number of Vandermonde Matrix')
plt.show()
