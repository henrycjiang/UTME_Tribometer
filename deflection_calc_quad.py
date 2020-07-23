#  File: defelection_calc_quad.py

#  Description: Calculates permutations of length, width, and thickness of quad cantilever beam that agrees with min and max deflection criteria and friction load

#  Name: Irene Lee

#  Date Created: 7/8/20

#  Date Last Modified: 7/14/20

from vars import *
import sys
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print()
print("Friction Load Input: ", Friction_Load/1e-3, 'mN')
print("Normal Load: ", Normal_Load/1e-3, 'mN')
print("Resulting Coefficient of Friction: ", Friction_Load/Normal_Load)
print()
print("Deflection Crteria")
print("  Max Deflection: ",deflection_max_hz/1e-3, 'mm')
print("  Min Deflection: ",deflection_min_hz/1e-3, 'mm')
print()

# initialize min and max deflections
max_def = 0
max_para = []

Inertia_Initial = (width_min * thickness_min**3)/12
min_def = ((Friction_Load*length_min**3)/(24*Emod*Inertia_Initial*inertia_factor))*2
min_para = []

l = length_max
t = thickness_min

#plt.axis([5.5, 7.5, .09, .12])
x = []
y = []
for w in width:
    Inertia = (w * t**3)/12
    deflection = ((Friction_Load*l**3)/(24*Emod*Inertia*inertia_factor))*2
    if (deflection >= deflection_min_hz) and (deflection <= deflection_max_hz):
        print("Deflection Criteria SATISFIED")
        print("Deflection: ",deflection/1e-3, 'mm')
        print("  l: ",round(l/1e-3,5), 'mm')
        print("  w: ",round(w/1e-3,5), 'mm')
        print("  t: ",round(t/1e-3,5), 'mm')
        print()
        x.append(w/1e-3)
        y.append(deflection/1e-3)
    if deflection > max_def:
        max_def = deflection
        max_para = [l,w,t]
    if deflection < min_def:
        min_def = deflection
        min_para = [l,w,t]   

if ((max_def <= deflection_max_hz) and (max_def >= deflection_min_hz)) or ((min_def <= deflection_max_hz) and (min_def >= deflection_min_hz)):
    print("Deflection Criteria SATISFIED")
else:
    print("Deflection Criteria NOT SATISFIED")
print()
print("Calculated Max Deflection: ",round(max_def/1e-3,4), 'mm') 
print("  l: ",round(max_para[0]/1e-3,4), 'mm')
print("  w: ",round(max_para[1]/1e-3,4), 'mm')
print("  t: ",round(max_para[2]/1e-3,4), 'mm')
print()
print("Calculated Min Deflection: ",round(min_def/1e-3,4), 'mm') 
print("  l: ",round(min_para[0]/1e-3,4), 'mm')
print("  w: ",round(min_para[1]/1e-3,4), 'mm')
print("  t: ",round(min_para[2]/1e-3,4), 'mm')
print()

#plot won't go through if samples don't meet input deflection criteria
plt.plot(x,y,linestyle='--', marker='o', color='b',label='2D model results')
#plt.plot(x_fea_hz,y_fea_hz, linestyle='--', marker='x', color='r',label='3D FEA results')
plt.xlabel("Width (mm)")
plt.ylabel("Deflection (mm)")
plt.title('Horizontal Beam Deflection with Changing Width')
plt.legend()
plt.show()     
