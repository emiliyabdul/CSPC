"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

x = 0.0
alp = 0.1
for _ in range(500):
    x_new = x - alp * df(x)
    if abs(x_new - x) < 1e-8:
        break
    x = x_new
min_gradient = x

min_newton = newton(df, x0=0, fprime=d2f)

min_slsqp = minimize(f, x0=0, method="SLSQP").x[0]

print(f"Gradient descent: x = {min_gradient:.6f}")
print(f"Newton's method:  x = {min_newton:.6f}")
print(f"SLSQP:            x = {min_slsqp:.6f}\n")


def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

for x0 in [0.0, 2.0]:
    print(f"=== 2B: g(x) from x0 = {x0} ===")

    x = x0
    alp = 0.02
    for _ in range(500):
        x_new = x - alp * dg(x)
        if abs(x_new - x) < 1e-8:
            break
        x = x_new
    min_gradient = x

    min_newton = newton(dg, x0=x0, fprime=d2g)
    curv = d2g(min_newton)
    kind = "minimum" if curv > 0 else "maximum"

    min_slsqp = minimize(g, x0=x0, method="SLSQP").x[0]

    print(f"Gradient descent: x = {min_gradient:.6f}")
    print(f"Newton's method:  x = {min_newton:.6f} (g''(x) = {curv:.2f} -> {kind})")
    print(f"SLSQP:            x = {min_slsqp:.6f}\n")