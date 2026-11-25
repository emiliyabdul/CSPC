# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
**What I built:**
- Added pytests to the negative decay rate, checked the agreement with the analytical decay law, provided a speed test to compare the NumPy to pure python.
**Speed comparison (loop vs NumPy):**
- loop : 3.4312 s
- numpy : 0.0003 s
- speed-up: 12047.46x faster
**Tests:** all passing? yes
**Conclusion:**
- The lesson learned out of testing the simulation - the average of any random process will eventually follow the predictable pattern, as for the technical part, I learned that the vectorization makes the calculations much faster and how the simulations can be tested by averaging different seed's (random) values.
## PW1 - Lab B: Data, Plotting, and Automation
**What I built:**
- Completed `plot.py`: it reads `decay_observed.csv` with `np.loadtxt` into `t` and `observed`, takes `N0` as the first observed count (5000), builds the analytical law `N0*exp(-0.3*t)`, and draws a 1x2 subplot with shared x and y axes (observed points on the left, analytical curve on the right), saved as `figure.png`.
- Wrote a `Snakefile` with a single `plot` rule (input `decay_observed.csv`, output `figure.png`, shell `python plot.py`).

**What the data showed:**
- 40 measurements from t = 0 to t = 19.5 s, the count falling from 5000 down to 17 - a fast drop at the start that flattens into a long tail, exactly the shape of exponential decay. With lambda = 0.3 the half-life is ln(2)/0.3 = 2.31 s, and the data does roughly halve over each such interval.

**Observed vs analytical:**
- The two panels match. On the same scale the scattered points sit on top of the smooth curve; the average relative deviation is about 6%, with the biggest relative gaps in the tail where the counts are small (e.g. 21 observed vs 16.7 predicted at t = 19) - that is counting noise, not a different law.

**Snakemake:**
- The pipeline rebuilds `figure.png` from `decay_observed.csv` by running `plot.py`, and because it compares timestamps it reruns only when the input (or the script) is newer than the figure - deleting `figure.png` made it rebuild, running it again with nothing changed did no work at all.

**Conclusion:**
- The observed decay follows the analytical law `N0*exp(-lambda*t)` well, with the only visible disagreement coming from the random noise in the low counts at late times. Automating the figure with Snakemake means the result can never silently go stale behind the data.

## PW2 - Lab A: Motion from Tracking Data
**What I built:**
- Completed `analysis.py`: it reads `freefall.csv` (81 samples, t = 0 to 7.9 s, height falling 500.0 m -> 194.6 m), differentiates the position once with `np.gradient` for velocity and again for acceleration, prints the mean and standard deviation of the acceleration, then integrates the noisy acceleration back with `cumulative_trapezoid` to recover velocity and position.
- Produced `motion.png`: three stacked panels sharing the time axis (position, velocity, acceleration) with a dashed reference line at -9.81 on the acceleration panel.
- Bonus: read `trajectory.csv`, plotted x(t), y(t) and the path, and computed the speed `sqrt(vx^2 + vy^2)` and the acceleration magnitude from `np.gradient` on each coordinate (`trajectory.png`, `velAcc.png`).

**Measured acceleration:**
- Mean acceleration: -8.580 m/s^2
- Standard deviation: 28.716 m/s^2 (individual values swing between about -73 and +55)
- The mean is in the right place for free fall - with a spread that large the uncertainty on the mean is about +/-3.2 m/s^2, so -8.58 and the true -9.81 are the same number as far as this data can tell.

**Why the acceleration is so noisy:**
- A derivative is a difference between nearby measurements divided by a small time step, so the sub-metre measurement noise in the position gets divided by 0.1 s twice over - two derivatives amplify it by roughly 1/dt^2, which is why the smooth-looking position (noise ~0.4 m) turns into a velocity that is already visibly rough and an acceleration whose scatter is several times larger than the signal itself.

**What integrating back showed:**
- Integrating the very noisy acceleration twice gave a position within **0.785 m** of the original measurements (largest difference over the whole 7.9 s), i.e. about 0.3% of the 306 m fallen. Because integration is a running sum, the random ups and downs cancel against each other instead of piling up.

**Bonus (2D trajectory):**
- The tracked path is a clean figure-eight (x completes one period in 20 s, y two), and the speed computed from the noisy coordinates stays in a bounded band - the first derivative is rough but still clearly readable, unlike the second.

**Conclusion:**
- Differentiation amplifies noise and integration suppresses it: the same dataset gave an acceleration too noisy to read point by point, yet integrating that same noisy acceleration reproduced the original trajectory to under a metre. The practical lesson is to trust averaged or integrated quantities from measured data, and to be sceptical of anything obtained by differentiating twice.
