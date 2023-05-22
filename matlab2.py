import numpy as np
## Given:
So = 1e-4# #channel bottom slope
h = 1# # m flow depth
g = 9.81# # m/s^2 gravitational acceleration
Delta = 2.65# # specific weight of the sediment/specific weight of water=specific gravity of sediment
nu = 1.01e-6# # m^2/s kinematic viscosity

## Find D = ?

u_star = np.sqrt(g*h*So) #shear velocity (m/s)
x_1 = np.divide(u_star**3,(Delta - 1))
x_2 = np.divide(x_1,nu)
x = np.divide(x_2, g) #critical sediment size
print(u_star)
print(x)
Re = np.roots([1, 33/7-18*x, 729/7-3510/7*x, -2916/7*x]) #Reynolds #
print(Re)
Re = max(np.real(Re)) #Feasible (real) Re root
print(Re)
left = np.multiply(nu,Re)
right = u_star
D = np.divide(left, right) #min diameter size of sediment needed
print(D)