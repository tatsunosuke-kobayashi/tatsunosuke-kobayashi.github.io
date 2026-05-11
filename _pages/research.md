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


Slab coexistence method
======

CO₂ solubility in water is evaluated using the slab (two-phase coexistence) method. A simulation cell with a water slab in the centre and CO₂-rich gas phases on both sides is equilibrated; CO₂ molecules partition spontaneously between the two phases, and the molality in the water region is read off as the equilibrium solubility at the imposed bulk-CO₂ pressure.

Below is an interactive trajectory: 25 snapshots from the last stage of a production run with **TIP4P/2005 water + TraPPE CO₂** at 50 bar, 298 K (3018 water molecules + 311 CO₂ molecules in a 31 × 31 × 283 Å cell).

<div id="ngl-slab-viewer" style="width: 100%; height: 520px; background: #f4f6f8; border: 1px solid #d6dae0; border-radius: 6px; position: relative;">
  <div id="ngl-slab-loading" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #4a5160; font-family: sans-serif;">
    Loading trajectory (~2 MB)...
  </div>
</div>
<p style="text-align: right; font-size: 0.85em; margin-top: 0.4em;">
  <a href="{{ base_path }}/files/co2_slab_last100.xyz.gz" download>Download the full 99-frame trajectory (.xyz.gz, ~9 MB)</a>
</p>

<script src="https://unpkg.com/ngl@2.0.0-dev.39/dist/ngl.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var stage = new NGL.Stage("ngl-slab-viewer", { backgroundColor: "#f4f6f8" });

  stage.loadFile("{{ base_path }}/files/co2_slab_last25.xyz.gz", {
    asTrajectory: true,
    defaultRepresentation: false
  }).then(function (comp) {
    var loading = document.getElementById("ngl-slab-loading");
    if (loading) loading.style.display = "none";

    comp.addRepresentation("ball+stick", {
      multipleBond: "symmetric",
      radiusScale: 0.35,
      aspectRatio: 1.5
    });

    if (comp.trajList && comp.trajList.length > 0) {
      var traj = comp.trajList[0];
      var player = new NGL.TrajectoryPlayer(traj.trajectory, {
        step: 1,
        timeout: 200,
        mode: "loop"
      });
      player.play();
    }

    stage.autoView();
  }).catch(function (err) {
    var loading = document.getElementById("ngl-slab-loading");
    if (loading) loading.textContent = "Failed to load trajectory: " + err.message;
  });

  window.addEventListener('resize', function () { stage.handleResize(); });
});
</script>


Fisher information geometry
======

Fisher information matrices computed over a 4-parameter cross-interaction LJ space (C–O<sub>w</sub> and O–O<sub>w</sub>, each in ε and σ). Across six force-field combinations and REDACTED, the stiff eigenvector — the direction that dominates the solubility response — is shared with ~REDACTED, suggesting a force-field-independent geometric structure of the correction.


Tools
======

Quantum ESPRESSO, DeePMD-kit, LAMMPS, MCCCS Towhee, ASE, VMD, NGL Viewer, PyTorch, custom Python.
