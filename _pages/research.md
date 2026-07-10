---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

Classical Force Field Optimization
======

<p style="color:#6b7383; font-style:italic; font-family:-apple-system, sans-serif;">Coming soon.</p>

CO₂–water slab simulation
======

<div id="slab-viewer" style="width: 100%; height: 560px; background: #0e1422; border-radius: 8px; position: relative; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12); overflow: hidden;">
  <div id="slab-loading" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #c8d1e0; font-family: -apple-system, sans-serif; font-size: 0.9em; letter-spacing: 0.04em; z-index: 5;">
    Loading trajectory…
  </div>
</div>

<p style="text-align: right; font-size: 0.82em; color: #6b7383; margin-top: 0.6em; font-family: -apple-system, sans-serif;">
  TIP4P/2005 + TraPPE · 50 bar · last 25 frames ·
  <a href="{{ base_path }}/files/co2_slab_last100.xyz.gz" download style="color: #0066cc;">download full trajectory</a>
</p>

<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var viewer = $3Dmol.createViewer("slab-viewer", {
    backgroundColor: 0x0e1422
  });

  fetch("{{ base_path }}/files/co2_slab_light.xyz")
    .then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.text();
    })
    .then(function (data) {
      var loading = document.getElementById("slab-loading");
      if (loading) loading.style.display = "none";

      viewer.addModelsAsFrames(data, "xyz", { noComputeSecondaryStructure: true });
      viewer.setStyle({}, { sphere: { scale: 0.55 } });
      viewer.zoomTo();
      viewer.render();
      viewer.animate({ loop: "forward", reps: 0, interval: 300 });
    })
    .catch(function (err) {
      console.error("[3Dmol] load error", err);
      var loading = document.getElementById("slab-loading");
      if (loading) loading.textContent = "Failed to load: " + (err.message || err);
    });
});
</script>

MLIP
======

<p style="color:#6b7383; font-style:italic; font-family:-apple-system, sans-serif;">Coming soon.</p>
