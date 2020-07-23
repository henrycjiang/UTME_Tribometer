#  File: vars.py

#  Description: Input variables for deflection_calc_quad and deflection_calc_dual

#  Name: Irene Lee

#  Date Created: 7/8/20

#  Date Last Modified: 7/14/20

# Length = 50 * 1e-3 # m
# Width = 10 * 1e-3 # m
# Thickness = 1 * 1e-3 # m

import numpy as np 

Emod = 68 * 1e9 # GPa to Pa //aluminum
Friction_Load = 25 * 1e-3 # mN to N 
Normal_Load = 100 * 1e-3 # mN to N
inertia_factor = .6 # fraction of how much the inertia of the beam would remain after drilling holes

length_min = 100 * 1e-3 # mm to m
length_max = 100 * 1e-3 # mm to m

width_min = 6 * 1e-3 # mm to m
width_max = 8 * 1e-3 # mm to m

thickness_min = .8 * 1e-3 # mm to m
thickness_max = .8 * 1e-3 # mm to m

length = list(np.arange(length_min,length_max,0.0001))
width = list(np.arange(width_min,width_max,0.0001))
thickness = list(np.arange(thickness_min,thickness_max,0.0001))

deflection_min = 0.35 *1e-3 # mm to m 
deflection_max = 0.45 * 1e-3 # mm to m 

x_fea_norm = [6,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8]
y_fea_norm = [.3547,.3547,.3547,.3547,.3547,.3547,.3547,.3547,.3547]