#  File: vars.py

#  Description: Calculates permutations of length, width, and thickness of dual cantilever beam that agrees with min and max deflection criteria and friction load

#  Name: Irene Lee

#  Date Created: 7/8/20

#  Date Last Modified: 7/14/20

from vars import *
import sys
import numpy as np 

print()
print("Friction Load Input: ", Friction_Load/1e-3, 'mN')
print("Maximum Normal Load: ", Normal_Load/1e-3, 'mN')
print("Resulting Coefficient of Friction: ", Friction_Load/Normal_Load)
print()
print("Deflection Crteria")
print("  Max Deflection: ",deflection_max/1e-3, 'mm')
print("  Min Deflection: ",deflection_min/1e-3, 'mm')
print()

# initialize min and max deflections
max_def = 0
max_para = []

Inertia_Initial = (width_min * thickness_min**3)/12
min_def = ((Friction_Load*length_min**3)/(24*Emod*Inertia_Initial*inertia_factor))*2
min_para = []

for l in length:
    for w in width:
        for t in thickness:
            Inertia = (w * t**3)/12
            deflection = ((Friction_Load*l**3)/(24*Emod*Inertia*inertia_factor))*2
            if (deflection >= deflection_min) and (deflection <= deflection_max):
                print("Deflection Criteria SATISFIED")
                print("Deflection: ",deflection/1e-3, 'mm')
                print("  l: ",round(l/1e-3,5), 'mm')
                print("  w: ",round(w/1e-3,5), 'mm')
                print("  t: ",round(t/1e-3,5), 'mm')
                print()
            if deflection > max_def:
                max_def = deflection
                max_para = [l,w,t]
            if deflection < min_def:
                min_def = deflection
                min_para = [l,w,t]

if ((max_def <= deflection_max) and (max_def >= deflection_min)) or ((min_def <= deflection_max) and (min_def >= deflection_min)):
    print("Deflection Criteria SATISFIED")
else:
    print("Deflection Criteria NOT SATISFIED")
print()
print("Calcualted Max Deflection: ",round(max_def/1e-3,4), 'mm') 
print("  l: ",round(max_para[0]/1e-3,4), 'mm')
print("  w: ",round(max_para[1]/1e-3,4), 'mm')
print("  t: ",round(max_para[2]/1e-3,4), 'mm')
print()
print("Calcualted Min Deflection: ",round(min_def/1e-3,4), 'mm') 
print("  l: ",round(min_para[0]/1e-3,4), 'mm')
print("  w: ",round(min_para[1]/1e-3,4), 'mm')
print("  t: ",round(min_para[2]/1e-3,4), 'mm')
print()

def moment_of_intertia(Width,Thickness):
    Inertia = (Width * Thickness**3)/12
    return Inertia

def delta(Friction_Load,Length,Emod,MomentofInertia):
    deflection = (Friction_Load*Length**3)/(24*Emod*Inertia)
    return deflection

def friction_coefficient(NormalLoad,FrictionLoad):
    u = (FrictionLoad)/(NormalLoad)
    return u

def percent_error_calc(deflection):
    percent = 0.02 / (deflection/1e-6) * 100
    return percent    

# Inertia = moment_of_intertia(Width, Thickness)
# deflection = delta(Friction_Load,Length,Emod,Inertia)
# u = friction_coefficient(Normal_Load,Friction_Load)
# percent_error = percent_error_calc(deflection)

# print()
# print('Inputs: ')
# print('Length: ', Length * 1e3, 'mm')
# print('Width: ', Width * 1e3, 'mm')
# print('Thickness: ', Thickness * 1e3, 'mm')
# print('Elastic Modulus: ', Emod * 1e-9, 'GPa')
# print('Friction Load: ', Friction_Load * 1e6, 'Micronewtons')
# print('Normal_Load: ', Normal_Load * 1e3, 'Millinewtons')

# print()
# print('Outputs: ')
# print('Moment of inertia: ', Inertia,  'm^(4)')
# print('Deflection:' , deflection/1e-6, 'micrometers +/- 0.02 micrometers')
# print('Coefficent of Friction:', u)
# print('Minimum Percent Error: ', percent_error, '%')
# print()
