import numpy as np

D = 0.00056 # Diameter (m)
nu = 1.01e-6 # kinematic viscosity m^2/s
D_star = ((2.65-1)*9.81/nu**2)**(1/3)*D #
print(D_star)
poly = [1, 195/7, 162/7-D_star**3/18, -11/42*D_star**3, -81/14*D_star**3]
R_starc = np.roots(poly)
R_starc = max(np.real(R_starc))
tau_starc = np.divide(R_starc**2,D_star**3)
tau_c = tau_starc*1.65*9810*D

print(R_starc)
print(tau_starc)
print(tau_c)
print('--------------------------------------------------------------------------------------------------------')

D = 0.00056 # Diameter (m)
nu = 1.01e-6 # kinematic viscosity m^2/s
Dsub=960*10**-3 #density of the plastic (g/cm^3)
DH20=1000 #density of water (g/cm^3)
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