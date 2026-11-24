"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

G = 9.81

t,y = np.loadtxt("freefall.csv", delimiter=",",skiprows=1, unpack=True)

v = np.gradient(y,t)
a = np.gradient(v,t)

print(f"Mean acceleration: {a.mean():.3f} m/s^2")
print(f"Std of acceleration: {a.std():.3f} m/s^2")


v_rec = cumulative_trapezoid(a,t,initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec,t,initial=0)+y[0]


max_diff = np.max(np.abs(y_rec-y))
print(f"{max_diff:.3f}")


#Plotting
fig,(pos,vel,acc) = plt.subplots(3,1,sharex=True,figsize=(8,8))

pos.plot(t,y, color="blue")
pos.set_title("Position VS Time")
pos.set_xlabel("Time")
pos.set_ylabel("Position")
pos.grid(True, linestyle=':', alpha=0.3)


vel.plot(t,v, color="green")
vel.set_title("Velocity VS Time")
vel.set_xlabel("Time")
vel.set_ylabel("Velocity")
vel.grid(True, linestyle=':', alpha=0.3)

acc.plot(t,a,color="yellow")
acc.axhline(-G,linestyle="--", color="red")
acc.set_title("Acceleration VS Time")
acc.set_xlabel("Time")
acc.set_ylabel("Acceleration")
acc.grid(True, linestyle=':', alpha=0.3)

fig.tight_layout()
fig.savefig("motion.png")

#Additional
t,xn,yn = np.loadtxt("trajectory.csv",delimiter=",",skiprows=1,unpack=True)

vx = np.gradient(xn,t)
vy = np.gradient(yn,t)

ax = np.gradient(vx,t)
ay = np.gradient(vy,t)

fig1, (xN,yN,path) = plt.subplots(3,1,figsize=(4,9))

xN.plot(t,xn,color="blue")
xN.set_title("Noisy X position")
xN.set_xlabel("Time")
xN.set_ylabel("X Position")

yN.plot(t,yn,color="green")
yN.set_title("Noisy Y position")
yN.set_xlabel("Time")
yN.set_ylabel("Y Position")

path.plot(xn,yn,color="orange")
path.set_title("Path")
path.set_xlabel("X Position")
path.set_ylabel("Y Position")

fig1.tight_layout()
fig1.savefig("trajectory.png")


speed1 = np.sqrt(vx**2+vy**2)
# speed2 = np.hypot(vx,vy)

accel1 = np.sqrt(ax**2+ay**2)
# accel2 = np.hypot(ax,ay)

# diffVel = speed1-speed2
# diffAcc = accel1-accel2

fig3, (speed,accel) = plt.subplots(1,2,sharex=True,figsize=(10,3))

speed.plot(t,speed1,color="green")
speed.set_title("Speed over time")
speed.set_xlabel("Time")
speed.set_ylabel("Speed")

accel.plot(t,accel1,color="red")
accel.set_title("Acceleration over time")
accel.set_xlabel("Time")
accel.set_ylabel("Acceleration")

fig3.tight_layout()
fig3.savefig("velAcc.png")










