---
permalink: /
title: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a master's student in the Department of Mechanical Engineering at **Keio University**, working with Prof. Kenji Yasuoka. My research sits at the intersection of **molecular simulation**, **machine learning**, and **statistical inference**, with the practical goal of making CO₂ solubility predictions for **carbon capture and storage (CCS)** quantitatively reliable at the molecular level.

I have applied for the **JSPS Research Fellowship for Young Scientists (DC1)** for the 2027 academic year, and plan to begin my Ph.D. at Keio in April 2027.


Research interests
======

- <i class="fas fa-atom" aria-hidden="true"></i> &nbsp;**Molecular simulation** of CO₂–water systems (classical MD / Monte Carlo, free-energy perturbation)
- <i class="fas fa-brain" aria-hidden="true"></i> &nbsp;**Machine learning interatomic potentials (MLIP)** for fluid-phase systems
- <i class="fas fa-chart-line" aria-hidden="true"></i> &nbsp;**Fisher information geometry** for force-field parameter identification
- <i class="fas fa-leaf" aria-hidden="true"></i> &nbsp;**Carbon capture and storage (CCS)** — molecular foundations of solubility prediction


Current research
======

Classical force fields systematically underestimate CO₂ solubility in water — by up to roughly 50 % in certain pressure / force-field combinations. During my master's work I have shown that, across **REDACTED** and **REDACTED**, the parameter direction that dominates the solubility correction is essentially shared across force fields (**REDACTED** in the REDACTED). My doctoral project will:

1. **Build on this preliminary finding** to derive a *universal REDACTED* using Fisher information geometry and REDACTED (PyTorch autograd).
2. **Develop a CO₂–water machine learning interatomic potential** trained on first-principles data, to evaluate the residual systematic errors that lie beyond the classical-force-field functional form.
3. **Partition the systematic error** — via Fisher analysis — into a REDACTED component (handled by classical-force-field tuning) and a REDACTED component (only visible through MLIP). This delivers a molecular-level account of CO₂ dissolution that directly addresses the reliability problem in CCS.


Tools
======

<i class="fas fa-cog" aria-hidden="true"></i> &nbsp;Quantum ESPRESSO &middot; DeePMD-kit &middot; LAMMPS &middot; MCCCS Towhee &middot; ASE &middot; PyTorch &middot; custom Python / Monte Carlo codes


Contact
======

Feel free to reach me at the email shown in the sidebar, or via GitHub. I'm always happy to talk about classical and ML-based molecular simulation, CCS, or applying statistical-geometric tools to physics.

---

*<small>This site is under construction; content will grow as the work progresses.</small>*
