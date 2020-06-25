# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:56:23 2020

@author: Henry Jiang
"""
import numpy
import sys

Custom_Emod = input('Custom Elastic Modulus?(y/n): ')

yes_list = ['yes', 'y', 'Yes', 'YES', 'Y']
no_list = ['no', 'No', 'n', 'N']

if Custom_Emod in yes_list:
    print("Satisfied")
    Emod_input = float(input("Input your Elastic Modulus in GPa (x.xx * 10^9): "))
    Emod = Emod_input * 1e9
        
elif Custom_Emod in no_list: 
    Emod = 200e9
    
else:
    print('You had one fucking job...')
    print('Exiting...Try again with y or n')    
    
    sys.exit()
            
Custom_Dimensions = input('Custom Dimensions?(y/n): ')

if Custom_Dimensions in yes_list:
    print('You will be prompted to enter new length, width, and thickness where thickness is the direction load is applied')
    # All calculations completed in SI units
    length = float(input('Beam length(mm): ')) * 1e-3
    width = float(input('Beam height(mm): ')) * 1e-3
    thickness = float(input('Beam thickness(mm): ')) * 1e-3
    
elif Custom_Dimensions in no_list:
    length = 150e-3
    width = 3e-3
    thickness = 0.5e-3
    
else:
    print('You had one fucking job...')
    print('Exiting...Try again with y or n')
    sys.exit()
    
Custom_Friction_Load = input('Custom friction load?(y/n): ')
    
if Custom_Friction_Load in yes_list:
    Friction_Load = float(input('Input your friction load in microNewtons(10^-6): ')) * 1e-6
    
elif Custom_Friction_Load in no_list:
    Friction_Load = 1.00 * 1e-6

else:
    print('You had one fucking job...')
    print('Exiting...Try again with y or n')
    sys.exit()
    
def moment_of_intertia_calc(width,thickness):
    I = (width * thickness**3)/12
    return I

def deflection(Load,Length,Modulus,MomentofInertia):
    # Simple cantilevered beam with point load simple assumption
    delta = (Load * Length**3)/(3 * Modulus * MomentofInertia)
    return delta

def percent_error_calc(deflection):
    percent = 0.02 / (deflection/1e-6) * 100
    return percent

I = moment_of_intertia_calc(width, thickness)
delta = deflection(Friction_Load,length,Emod,I)
percent_error = percent_error_calc(delta)

print('Moment of inertia: ', I)
print('Deflection:' , delta/1e-6, 'microns +/- 0.02 microns')
print('Minimum Percent Error: ', percent_error, '%')

    
    