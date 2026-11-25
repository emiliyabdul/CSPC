"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

def k_imbalance(x):
        equil = ((2*x)**2)/((a-x)*(b-x))
        return equil-K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

kmin_newton = newton(k_imbalance,x0=0.5)
print(f"The root by newton's method: {kmin_newton}")

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.

min_Err = minimize(lambda x: k_imbalance(x[0])**2,x0=[0.5],method="SLSQP",bounds=[(0,0.999)])
kmin_slsqp = min_Err.x[0]
print(f"The root by SLSQP: {kmin_slsqp}")


# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

nH2Eq = 1-kmin_newton
nI2Eq = 1-kmin_newton
nHIEq = 2*kmin_newton
print(f"Equilibrium amounts: {nH2Eq:.2f}, {nI2Eq:.2f}, {nHIEq:.2f}")

x = np.linspace(0,1,100)
nH2 = 1-x
nI2 = 1-x
nHI = 2*x

fig, depen = plt.subplots(1,1,figsize=(5,5))

depen.plot(x,nH2,color="blue")
depen.plot(x,nI2,"--", color="orange")
depen.plot(x,nHI,color="green")
depen.axhline(kmin_newton,linestyle="--", color="red")
depen.set_title("Reagents VS Product")
depen.set_xlabel("X amount")
depen.set_ylabel("COncentration")

fig.tight_layout()
fig.savefig("equilibrium.png")
