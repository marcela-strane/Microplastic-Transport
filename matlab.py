import numpy as np
import os
import csv

'''#Matlab code turned into Python code (by Marcela) emailed to me by Junko Guo Paper: Emperical Model for Shields Diagram and Its Applications
#D = 0.00056 # Diameter (m)
#nu = 1.01e-6 # kinematic viscosity m^2/s
#D_star = ((2.65-1)*9.81/nu**2)**(1/3)*D 
#print(D_star)
#poly = [1, 195/7, 162/7-D_star**3/18, -11/42*D_star**3, -81/14*D_star**3]
#R_starc = np.roots(poly)
#R_starc = max(np.real(R_starc))
#tau_starc = np.divide(R_starc**2,D_star**3)
#tau_c = tau_starc*1.65*9810*D

#print(R_starc)
#print(tau_starc)
#print(tau_c)
#print('--------------------------------------------------------------------------------------------------------')
'''


#Marcela's continuation of the  matlab code to be clearer and applicable to her project
D = 0.00056 # Diameter (m)
nu = 1.01e-6 # kinematic viscosity m^2/s

# Loop through different plastic densities

filename= "PlasticDens.csv"
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[-1] != 'Density (g/cm^3)':
            print(row[-1])
            Dsub=float(row[-1]) #density of the plastic (g/cm^3)
            
            DH20=1 #density of water (g/cm^3)
            delta=Dsub/DH20 #specific gravity= density of substance/density of water
            g=9.81 #m/s^2 gravity
            D_star = ((delta-1)*g/nu**2)**(1/3)*D #Dimensionless sediment/particle diameter
            print(D_star)
            poly = [1, 195/7, 162/7-D_star**3/18, -11/42*D_star**3, -81/14*D_star**3]
            R_starc = np.roots(poly)
            R_starc = max(np.real(R_starc))
            tau_starc = np.divide(R_starc**2,D_star**3)
            tau_c = tau_starc*1.65*9810*D

            print(R_starc)
            print(tau_starc)
            print(tau_c)