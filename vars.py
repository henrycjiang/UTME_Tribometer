#  File: vars.py

#  Description: Input variables for deflection_calc_quad and deflection_calc_dual

#  Name: Irene Lee

#  Date Created: 7/8/20

#  Date Last Modified: 7/27/20

# Length = 50 * 1e-3 # m
# Width = 10 * 1e-3 # m
# Thickness = 1 * 1e-3 # m

import numpy as np 

Emod = 68 * 1e9 # GPa to Pa //aluminum
Friction_Load = 25 * 1e-3 # mN to N 
Normal_Load = 100 * 1e-3 # mN to N
inertia_factor = .6 # fraction of how much the inertia of the beam would remain after drilling holes

length_min = 140 * 1e-3 # mm to m
length_max = 150 * 1e-3 # mm to m

width_min = 6 * 1e-3 # mm to m
width_max = 8 * 1e-3 # mm to m

thickness_min = .8 * 1e-3 # mm to m
thickness_max = .8 * 1e-3 # mm to m

length = list(np.arange(length_min,length_max,0.0001))
width = list(np.arange(width_min,width_max,0.0001))
thickness = list(np.arange(thickness_min,thickness_max,0.0001))

#deflection criteria for vertical beam, normal load
deflection_min_vert= 0.35 *1e-3 # mm to m 
deflection_max_vert = 0.45 * 1e-3 # mm to m 

#deflection criteria for horizonal beam, friction load
deflection_min_hz= 0.15 *1e-3 # mm to m 
deflection_max_hz = 0.25 * 1e-3 # mm to m 

# x = width and y = deflection FEA results for vertical beam
x_fea_vert = [6,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8]
y_fea_vert = [0.3769,0.3712,0.365, 0.3593,0.3532,0.3477,0.3411,0.3368, 0.3310]

# x = width and y = deflection FEA results for horizontal beam
x_fea_hz = [6,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8]
y_fea_hz = [0.2035,0.2005,0.1974,0.1945,0.1915,0.1886,0.1858,0.1834,0.1810]