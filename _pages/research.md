---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

CO₂–water slab simulation
======

<div id="ngl-slab-viewer" style="width: 100%; height: 560px; background: #0e1422; border-radius: 8px; position: relative; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12); overflow: hidden;">
  <div id="ngl-slab-loading" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #c8d1e0; font-family: -apple-system, sans-serif; font-size: 0.9em; letter-spacing: 0.04em;">
    Loading trajectory…
  </div>
</div>

<p style="text-align: right; font-size: 0.82em; color: #6b7383; margin-top: 0.6em; font-family: -apple-system, sans-serif;">
  TIP4P/2005 + TraPPE · 50 bar · last 25 frames ·
  <a href="{{ base_path }}/files/co2_slab_last100.xyz.gz" download style="color: #0066cc;">download full trajectory</a>
</p>

<script src="https://unpkg.com/ngl@2.0.0-dev.39/dist/ngl.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var stage = new NGL.Stage("ngl-slab-viewer", { backgroundColor: "#0e1422" });

  stage.loadFile("{{ base_path }}/files/co2_slab_last25.xyz.gz", {
    asTrajectory: true,
    defaultRepresentation: false
  }).then(function (comp) {
    var loading = document.getElementById("ngl-slab-loading");
    if (loading) loading.style.display = "none";

    comp.addRepresentation("ball+stick", {
      multipleBond: "symmetric",
      radiusScale: 0.32,
      aspectRatio: 1.5
    });

    if (comp.trajList && comp.trajList.length > 0) {
      var traj = comp.trajList[0];
      var player = new NGL.TrajectoryPlayer(traj.trajectory, {
        step: 1,
        timeout: 220,
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
