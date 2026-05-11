---
permalink: /
title: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a master's student in the Department of Mechanical Engineering, Keio University, working with Prof. Kenji Yasuoka. My research focuses on the **molecular-level prediction of carbon dioxide (CO₂) solubility in water**, motivated by the need for reliable simulation tools in carbon capture and storage (CCS).

I am applying for the JSPS Research Fellowship for Young Scientists (DC1) for the 2027 academic year. From April 2027, I plan to start my Ph.D. program at Keio University.

Research interests
======

- **Molecular simulation** of CO₂–water systems (classical MD/MC, free energy perturbation)
- **Machine learning interatomic potentials (MLIP)** for fluid-phase systems
- **Fisher information geometry** applied to force field parameter identification
- **Carbon capture and storage (CCS)** — molecular foundations of CO₂ solubility prediction

Current research
======

Classical force fields systematically underestimate CO₂ solubility in water (up to ~50% in certain pressure/force-field combinations). During my master's research, I have shown that across REDACTED and REDACTED, the parameter direction that dominates the solubility correction is essentially shared across force fields (REDACTED in REDACTED). My doctoral project will:

1. Build on this preliminary finding to derive a **universal REDACTED** via Fisher information geometry and REDACTED (with PyTorch autograd).
2. Develop a **CO₂–water machine learning interatomic potential** trained on first-principles data to evaluate the residual systematic errors that lie beyond the classical-force-field functional form.
3. Use Fisher analysis to **partition the systematic error** into a REDACTED component (via classical force-field tuning) and a REDACTED component (visible only through MLIP), providing a molecular-level account of CO₂ dissolution relevant to CCS.

Tools I work with
======

Quantum ESPRESSO (DFT) · DeePMD-kit (MLIP training) · LAMMPS (MD) · MCCCS Towhee (MC) · ASE · PyTorch · custom Python / Monte Carlo scripts.

Contact
======

Feel free to reach me at the email address shown in the sidebar.

*This site is under construction.*
