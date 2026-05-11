---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

I work on molecular simulation of CO₂–water systems, with two coupled research axes:

1. **Fisher information geometry for force-field calibration** — identifying the parameter directions that dominate CO₂ solubility error and turning empirical correction into a derived, generalizable rule.
2. **Machine learning interatomic potentials (MLIP)** — building DFT-accurate models of CO₂–water interactions to evaluate the residual error that lies beyond the classical functional form.

The motivation is carbon capture and storage (CCS): classical force fields systematically underestimate CO₂ solubility, and high-pressure measurements are experimentally difficult.


CO₂ solubility in water across classical force fields
======

Six water/CO₂ force-field combinations evaluated at REDACTED. All combinations underestimate the experimental reference at higher pressures, with up to ~50 % deviation in the worst case.


Fisher information geometry
======

Fisher information matrices computed over a 4-parameter cross-interaction LJ space (C–O<sub>w</sub> and O–O<sub>w</sub>, each in ε and σ). Across six force-field combinations and REDACTED, the stiff eigenvector — the direction that dominates the solubility response — is shared with ~REDACTED, suggesting a force-field-independent geometric structure of the correction.


CO₂–water simulation cells (VMD)
======

Snapshots from production GEMC / MD simulations of CO₂–water at representative pressure conditions, visualized with VMD.

*Snapshots will appear here once rendering is finalized.*


Tools
======

Quantum ESPRESSO, DeePMD-kit, LAMMPS, MCCCS Towhee, ASE, VMD, PyTorch, custom Python.
