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

arrayX=[]
arrayY=[]

filename= "PlasticDens.csv"
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    
    for row in datareader:
        if row[-1] != 'Density (g/cm^3)':
            print(f"Density {row[0]}:{row[-1]}") #last column with the density of the plastic
            Dsub=float(row[-1]) #density of the plastic (g/cm^3)
            
            DH20=1 #density of water (g/cm^3)
            delta=Dsub/DH20 #specific gravity= density of substance/density of water
            g=9.81 #m/s^2 gravity
            D_star = ((delta-1)*g/nu**2)**(1/3)*D #Dimensionless sediment/particle diameter
            print(f"Dimensionless particle diameter:{D_star}")
            poly = [1, 195/7, 162/7-D_star**3/18, -11/42*D_star**3, -81/14*D_star**3]
            R_starc = np.roots(poly)
            R_starc = max(np.real(R_starc)) #critical grain reynolds number
            tau_starc = np.divide(R_starc**2,D_star**3) #critical shields parameter or dimensionless critical shear stress
            tau_c = tau_starc*1.65*9810*D #dimensional critical shear stress (i think this is shear stress of the bed)

            print(f"Critical Grain Reynolds Number:{R_starc}")
            print(f"Critical Shields parameter:{tau_starc}")
            print(f"dimensional critical shear stress:{tau_c}")
            if Dsub >= 1:  
                arrayX.append(D_star)
                arrayY.append(tau_starc)

import matplotlib.pyplot as plt
# plotting the points 
plt.plot(arrayX, arrayY, 'o')
# naming the x axis
plt.xlabel('Re')
# naming the y axis
plt.ylabel('Shields Parameter')
# giving a title to my graph
plt.title('Marcis theoretical data!')
# function to show the plot
plt.show()

print('----------------------------------------------------------------')
from matplotlib.ticker import ScalarFormatter
# Create a figure and an axes
fig, ax = plt.subplots()

# Plot data
ax.plot(arrayX, arrayY, 'o')

# Set scale to logarithmic for both axes
ax.set_xscale('log')
ax.set_yscale('log')

# Use ScalarFormatter, setting scientific notation with the power of 10
formatter = ScalarFormatter(useMathText=True)  # useMathText to get the 10^x format
formatter.set_scientific(False)
formatter.set_powerlimits((-2, 3))  # This will use scientific notation everywhere

# Apply the formatter to both axes
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

# Set labels (optional)
ax.set_xlabel('X axis (log scale)')
ax.set_ylabel('Y axis (log scale)')

# Display the plot
plt.show()

print('--------------------goral et al data------------------')

X=[1.1,1.1,1.5,0.6,1.7,1.8,1.1,1.1,1.2,1.2,1.2,1.2,1.3,1.4,1.4,1.6,1.7,1.6,1.9,1.9,1.9,1.9,1.8,2,1.9,1.9,1.2,1.3,1.4,1.2,1.5,1.6,1.3,1.2,1.2,1.1,1.3,1.3,1.2,1.5,1.4,1.5,1.6,1.6,1.4,1.7,1.7,1.7,1.7,1.8,1.3,1.3,1.3,0.9,0.9,1,0.9]
Y=[0.012,0.006,0.0071,0.0056,0.0068,0.0057,0.0078,0.0052,0.0055,0.0063,0.0063,0.0058,0.0065,0.006,0.0058,0.012,0.01,0.0093,0.0091,0.011,0.0093,0.0097,0.0086,0.0088,0.0081,0.008,0.008,0.0066,0.0067,0.0067,0.006,0.0058,0.0072,0.0087,0.011,0.0073,0.0082,0.0081,0.007,0.008,0.0066,0.0073,0.0069,0.0064,0.0092,0.01,0.0091,0.0092,0.0083,0.0075,0.02,0.017,0.013,0.011,0.0079,0.011,0.0066]

#X.sort()
#Y.sort()

plt.plot(X, Y, 'o')
plt.show()
