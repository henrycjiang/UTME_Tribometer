#  File: deflection_calc_dual.py

#  Description: Calculates permutations of length, width, and thickness of dual cantilever beam that agrees with min and max deflection criteria and friction load

#  Name: Irene Lee

#  Date Created: 7/22/20

#  Date Last Modified: 7/27/20

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
print("  Max Deflection: ",deflection_max_vert/1e-3, 'mm')
print("  Min Deflection: ",deflection_min_vert/1e-3, 'mm')
print()

# initialize min and max deflections
max_def = 0
max_para = []

Inertia_Initial = (width_min * thickness_min**3)/12
min_def = (Normal_Load*length_min**3)/(24*Emod*Inertia_Initial*inertia_factor)
min_para = []

l = length_max
t = thickness_min

#plt.axis([5.5, 7.5, .09, .12])
x = []
y = []
for w in width:
    Inertia = (w * t**3)/12
    deflection = (Normal_Load*l**3)/(24*Emod*Inertia*inertia_factor)

    if (deflection >= deflection_min_vert) and (deflection <= deflection_max_vert):
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

if ((max_def <= deflection_max_vert) and (max_def >= deflection_min_vert)) or ((min_def <= deflection_max_vert) and (min_def >= deflection_min_vert)):
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

# Linear Regression Analysis
linReg_3D = LinearRegression()

lin_x = np.array(x_fea_vert).reshape(-1,1)
lin_y = np.array(y_fea_vert)

# fits the linear regression
linReg_3D.fit(lin_x, lin_y)
# print results
print('3D Model Regression')
print('Coefficient of Determination: ',linReg_3D.score(lin_x,lin_y))
print('Slope: ',linReg_3D.coef_)
print('Intercept: ',linReg_3D.intercept_)
print()

# linear regression funcion 
def lin_reg_func(x, m, b):
    return m*x + b

x_plot = np.arange(6,6.9,.1)

#plot won't go through if samples don't meet input deflection criteria
fig = plt.figure(figsize=(15,8))
plt.plot(x,y,linestyle='--', marker='o', color='b',label='2D model results')
plt.plot(x_fea_vert,y_fea_vert, linestyle='--', marker='x', color='r',label='3D FEA results')
plt.plot(x_plot,lin_reg_func(x_plot,linReg_3D.coef_,linReg_3D.intercept_),label='3D Linear Regression')
plt.text(6.7, .34, 'y = '+ str(round(linReg_3D.coef_[0],4)) +'x' + " + " + str(round(linReg_3D.intercept_,4)) +'\n$R^2$ = ' + str(round(linReg_3D.score(lin_x,lin_y),4)) , fontsize=15)
plt.xlabel("Width (mm)")
plt.ylabel("Deflection (mm)")
plt.title('Vertical Beam Deflection with Changing Width')
plt.legend()
plt.show() 