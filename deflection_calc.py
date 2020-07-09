#  File: vars.py

#  Description: Calculates double beam deflection

#  Name: Irene Lee

#  Date Created: 7/8/20

#  Date Last Modified: 7/9/20

from vars import *
import sys

def moment_of_intertia(Width,Thickness):
    Inertia = (Width * Thickness**3)/12
    return Inertia

def delta(Friction_Load,Length,Emod,MomentofInertia):
    total_deflection = (Friction_Load*Length**3)/(24*Emod*Inertia)
    # double cantilevered beam is approx (1/8) of the single fixed end beam 
    deflection = total_deflection*(1/8) 
    return deflection

def friction_coefficient(NormalLoad,FrictionLoad):
    u = (FrictionLoad)/(NormalLoad)
    return u

def percent_error_calc(deflection):
    percent = 0.02 / (deflection/1e-6) * 100
    return percent    

Inertia = moment_of_intertia(Width, Thickness)
deflection = delta(Friction_Load,Length,Emod,Inertia)
u = friction_coefficient(Normal_Load,Friction_Load)
percent_error = percent_error_calc(deflection)

print()
print('Inputs: ')
print('Length: ', Length * 1e3, 'mm')
print('Width: ', Width * 1e3, 'mm')
print('Thickness: ', Thickness * 1e3, 'mm')
print('Elastic Modulus: ', Emod * 1e-9, 'GPa')
print('Friction Load: ', Friction_Load * 1e6, 'Micronewtons')
print('Normal_Load: ', Normal_Load * 1e3, 'Millinewtons')
print()

print()
print('Outputs: ')
print('Moment of inertia: ', Inertia,  'm^(4)')
print('Deflection:' , deflection/1e-6, 'microns +/- 0.02 microns')
print('Coefficent of Friction:', u)
print('Minimum Percent Error: ', percent_error, '%')
print()
