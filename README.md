# IAIFI Symbolic Regression Hackathon

Hackathon from the 2026 IAIFI summer school.
Look at https://github.com/munozariasjm/sr_tutorial_material for the tutorial material, and the `hackathon.ipynb` notebook for getting started.

## Equation Hunting in Gaia.
The data is a table of Gaia DR3 stars with full 6D phase-space coordinates (positions, proper motions, radial velocities, and propagated uncertainties) https://doi.org/10.5281/zenodo.8088365. A snapshot of a collisionless system already contains its dynamics as in equilibrium the collisionless Boltzmann equation relates the phase-space density f(x,v), which the stars sample directly, to the Galactic potential Φ(x), which nobody can measure, stellar accelerations here are of order 1 cm/s/yr.
Your task is using the template-and-derivative machinery from the tutorial, plus any preprocessing you like, search jointly for a closed-form f and Φ that kill this residual while f still describes the stars you were given. There is no ground truth, the potential of the Galaxy is genuinely unknown, and nobody knows the best achievable score. Existing work represents Φ with a neural network, so a compact symbolic form that scores competitively would be new, and a good enough equation could lead to a paper. Hold out your own test split to verify anything you find.


### Some References
- https://arxiv.org/abs/2507.03742
- https://iopscience.iop.org/article/10.3847/1538-4357/aca3a7
- https://arxiv.org/abs/2402.00108