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
* B.S., Mechanical Engineering, Keio University, 2024

Research interests
======
* Molecular simulation of CO₂–water systems
* Machine learning interatomic potentials
* Fisher information geometry for force-field calibration
* Carbon capture and storage

Technical skills
======
* **Simulation**: LAMMPS, MCCCS Towhee, Quantum ESPRESSO, DeePMD-kit, ASE
* **Programming**: Python (PyTorch, NumPy), Bash
* **HPC**: GPU-based MLIP training, SLURM, conda

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
* Co-founder and co-representative of a student club at Keio University (2025–)
