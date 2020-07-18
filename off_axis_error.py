# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:47:45 2020

@author: Henry Jiang
"""
from mpl_toolkits.mplot3d import Axes3D  
from numpy import sin, cos, deg2rad, meshgrid, linspace
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def off_axis_calc(Ffriction, Fnormal, alpha, beta):

    alpha_rad = deg2rad(alpha)
    beta_rad = deg2rad(beta)
    
    Fx = (Ffriction * cos(alpha_rad)) + (Fnormal * sin(alpha_rad))
    Fy = (Fnormal * cos(beta_rad)) - (Ffriction * sin(beta_rad))
    mu = (Fx * cos(beta_rad) - Fy * sin(alpha_rad))/(Fy * cos(alpha_rad) + Fx * sin(beta_rad) )
    Error  = ( mu  * cos(beta_rad) - mu**2 * sin(beta_rad) - mu * cos(alpha_rad) - sin(alpha_rad))/( mu * cos(beta_rad) - mu**2 * sin(beta_rad) )
    Error = abs(Error) * 100
    
    return Error
    
'''
Ffriction = 1e-6 # 1 micronewton
Fnormal = 1e-3 # 1 milinewton
alpha = 0.01 # Reasonable 0.1 degrees offset
beta = 0.01 # Also reasonable offset
print("The coeff of friction is: ", z[0])
print("The percent error is: ", abs(z[1]) * 100, "%")

'''

Ffriction = 5e-6 # 1 micronewton
Fnormal = 1e-3 # 1 milinewton
alpha = linspace(0,0.1,100)
beta = linspace(0,0.1,100)

fig = plt.figure()
ax = fig.gca(projection='3d')

X, Y = meshgrid(alpha, beta) 
# X corresp to alpha, Y corresp to beta
Z = off_axis_calc(Ffriction, Fnormal, X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0,80)
ax.set_xlabel("Alpha")
ax.set_ylabel("Beta")
ax.set_zlabel("Percent Error")
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()