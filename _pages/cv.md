---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* M.S., Mechanical Engineering, Keio University, 2027 (expected)
* B.S., Mechanical Engineering, Keio University, 2025
  * Cumulative GPA: 3.6 / 4.0

Research interests
======
* Molecular simulation of CO₂–water systems (classical MD/MC, free energy perturbation)
* Machine learning interatomic potentials (MLIP) for fluid-phase systems
* Fisher information geometry for force field parameter identification
* Carbon capture and storage (CCS) — molecular foundations of solubility prediction

Technical skills
======
* **Simulation**: LAMMPS, MCCCS Towhee, ASE, Quantum ESPRESSO, DeePMD-kit
* **Programming**: Python (NumPy, PyTorch, automatic differentiation), Bash, custom Monte Carlo / FEP codes
* **HPC**: GPU-based MLIP training, SLURM job management, conda environments
* **Theory**: Statistical mechanics, free energy perturbation, Fisher information geometry, neural network potentials

Honors and fellowships
======
*To be updated as available.*

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

Activities
======
* Co-founder and co-representative of a student club at Keio University (since 2025)

*Last updated: May 2026. Site under construction.*
