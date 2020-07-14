#  File: vars.py

#  Description: Input variables for deflection_calc.py

#  Name: Irene Lee

#  Date Created: 7/8/20

#  Date Last Modified: 7/14/20

# Length = 50 * 1e-3 # m
# Width = 10 * 1e-3 # m
# Thickness = 1 * 1e-3 # m

import numpy as np 

Emod = 68 * 1e9 # GPa to Pa //aluminum
Friction_Load = 10 * 1e-3 # mN to N 
Normal_Load = 100 * 1e-3 # mN to N
inertia_factor = 0.5 # fraction of how much the inertia of the beam would be reduced after drilling holes

length_min = 40 * 1e-3 # mm to m
length_max = 150 * 1e-3 # mm to m

width_min = 4 * 1e-3 # mm to m
width_max = 15 * 1e-3 # mm to m

thickness_min = 1 * 1e-3 # mm to m
thickness_max = 2 * 1e-3 # mm to m

length = list(np.arange(length_min,length_max,0.0001))
width = list(np.arange(width_min,width_max,0.0001))
thickness = list(np.arange(thickness_min,thickness_max,0.0001))

deflection_min = 1.5 *1e-3 # mm to m 
deflection_max = 2 * 1e-3 # mm to m 
