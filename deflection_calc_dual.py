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

# 3D Linear Regression Analysis
linReg_3D = LinearRegression()

lin_x = np.array(x_fea_vert).reshape(-1,1)
lin_y = np.array(y_fea_vert)

# fits 3D linear regression
linReg_3D.fit(lin_x, lin_y)
# print results
print('3D Model Regression')
print('Coefficient of Determination: ',linReg_3D.score(lin_x,lin_y))
print('Slope: ',linReg_3D.coef_[0])
print('Intercept: ',linReg_3D.intercept_)
print()

# linear regression funcion 
def lin_reg_func3D(x, m, b):
    return m*x + b

x_plot = np.arange(6,6.9,.1)


# 2D Linear Regression Analysis
linReg_2D = LinearRegression()

lin_x2 = np.array(x).reshape(-1,1)
lin_y2 = np.array(y)

# fits 2D linear regression
linReg_2D.fit(lin_x2, lin_y2)
# print results
print('2D Model Regression')
print('Coefficient of Determination: ',linReg_2D.score(lin_x2,lin_y2))
print('Slope: ',linReg_2D.coef_[0])
print('Intercept: ',linReg_2D.intercept_)
print()

# linear regression funcion 
def lin_reg_func2D(x2, m2, b2):
    return m2*x2 + b2

x_plot2 = np.arange(6,6.9,.1)

# calculates y-int offset between 2D and 3D model 
y_off = linReg_2D.intercept_ - linReg_3D.intercept_
print('y-intercept offset: ',y_off)

# error calculations
difference = []
zip_object = zip(y, y_fea_vert)
for y_i, y_fea_vert_i in zip_object:
    difference.append(y_i-y_fea_vert_i)

div = []
zip_object = zip(difference, y_fea_vert)
for difference_i, y_fea_vert_i in zip_object:
    div.append(difference_i/y_fea_vert_i)

res =  [abs(ele) for ele in div] 
multiplied_list = [element * 100 for element in res]

print('Max error: ', max(multiplied_list))
print('Min error: ', min(multiplied_list))


#plot won't go through if samples don't meet input deflection criteria
fig = plt.figure(figsize=(15,8))
#plotting 2D and 3D data
plt.plot(x,y,linestyle='--', marker='o', color='b',label='2D model results')
plt.plot(x_fea_vert,y_fea_vert, linestyle='--', marker='x', color='r',label='3D FEA results')
#plotting 3D linear regression and equations
plt.plot(x_plot,lin_reg_func3D(x_plot,linReg_3D.coef_,linReg_3D.intercept_),label='3D Linear Regression')
plt.text(6.65, .3, 'y = '+ str(round(linReg_3D.coef_[0],4)) +'x' + " + " + str(round(linReg_3D.intercept_,4)) +'\n$R^2$ = ' + str(round(linReg_3D.score(lin_x,lin_y),4)) , fontsize=10)
#plotting 2D linear regression and equations
plt.plot(x_plot2,lin_reg_func2D(x_plot2,linReg_2D.coef_,linReg_2D.intercept_),label='2D Linear Regression')
plt.text(6.6, .4, 'y = '+ str(round(linReg_2D.coef_[0],4)) +'x' + " + " + str(round(linReg_2D.intercept_,4)) +'\n$R^2$ = ' + str(round(linReg_2D.score(lin_x2,lin_y2),4)) , fontsize=10)
#labeling y-intercept offset on the graph
plt.text(6.6, .38, 'y-intercept offset = '+ str(round(y_off,4)), fontsize=10)
#scaling plot
plt.ylim(0, .45)
plt.xticks(np.arange(6, 6.9, step=0.1))
#title and axis labels
plt.xlabel("Width (mm)")
plt.ylabel("Deflection (mm)")
plt.title('Vertical Beam Deflection with Varying Width')
plt.legend()
plt.show() 