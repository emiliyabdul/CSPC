"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.

V,pH = np.loadtxt("titration.csv",delimiter=",",skiprows=1,unpack=True)

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.

slopepH = np.gradient(pH,V)
idV = np.argmax(slopepH)
Vequil = V[idV]
print(f"Equivalence point volume: {Vequil:.2f}")


# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.

fig,(pHV,slopeV) = plt.subplots(1,2,sharex=True,figsize=(9,4))

pHV.plot(V,pH,color="blue")
pHV.axvline(Vequil,linestyle=":",color="red",label="Equivalence point")
pHV.grid(True,linestyle=":",alpha=0.3)
pHV.set_title("pH vs volume")
pHV.set_xlabel("volume")
pHV.set_ylabel("pH")
pHV.legend()

slopeV.plot(V,slopepH,color="green")
slopeV.axvline(Vequil,linestyle=":",color="red",label="Equivalence point")
slopeV.grid(True,linestyle=":",alpha=0.3)
slopeV.set_title("slope vs volume")
slopeV.set_xlabel("volume")
slopeV.set_ylabel("slope")
slopeV.legend()

fig.tight_layout()
fig.savefig("titration.png")