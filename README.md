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