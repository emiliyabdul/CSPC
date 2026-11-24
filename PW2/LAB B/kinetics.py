"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.

t,c = np.loadtxt("kinetics.csv",delimiter=",",skiprows=1,unpack=True)
C0 = c[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.

def total_error(k):
    predicted = C0*np.exp(-k*t)
    return np.sum((c-predicted)**2)
    

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.

res = minimize(total_error, x0=0.5,method="SLSQP",bounds=[(0,5)])
best_fit = res.x[0]
print(f"Rate: {best_fit}")

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.

fitted = C0*np.exp(-best_fit*t)
fig, data = plt.subplots(1,1,figsize=(4,5))

data.scatter(t,c,color="blue")
data.plot(t,fitted,color="red")
data.set_title("Measured VS Fitted")

fig.tight_layout()
fig.savefig("kinetics.png")