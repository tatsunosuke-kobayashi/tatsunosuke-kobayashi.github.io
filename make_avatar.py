#!/usr/bin/env python3
"""最小構成アバター: CO2 ロッドで T(2本)・K(4本) を組み、分岐点を H2O コネクタに。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

BG_IN  = "#1b3a5e"; BG_OUT = "#0c1b30"
O_COL  = "#E8412E"; H_COL  = "#EDEDED"; C_COL = "#8A9099"; BOND = "#C2C9D4"

FIG = 9.0
fig, ax = plt.subplots(figsize=(FIG, FIG), dpi=100)
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_aspect("equal"); ax.axis("off")

# 背景グラデ
grad = np.zeros((400, 400, 3)); yy, xx = np.mgrid[0:400, 0:400]
r = np.clip(np.sqrt((xx-200)**2 + (yy-200)**2)/200.0, 0, 1)
c_in  = np.array([int(BG_IN[i:i+2],16) for i in (1,3,5)])/255
c_out = np.array([int(BG_OUT[i:i+2],16) for i in (1,3,5)])/255
for k in range(3): grad[:,:,k] = c_in[k]*(1-r)+c_out[k]*r
ax.imshow(grad, extent=[0,10,0,10], origin="lower", zorder=0, interpolation="bilinear")

def atom(x, y, rad, color, z):
    ax.add_patch(Circle((x+0.035, y-0.035), rad, facecolor="#000", alpha=0.28,
                        edgecolor="none", zorder=z))
    ax.add_patch(Circle((x, y), rad, facecolor=color, edgecolor="#0d1b2e",
                        lw=0.7, zorder=z+1))
    ax.add_patch(Circle((x-rad*0.32, y+rad*0.32), rad*0.30, facecolor="#fff",
                        alpha=0.55, edgecolor="none", zorder=z+2))

def bond(x1, y1, x2, y2, z, w):
    ax.plot([x1,x2],[y1,y2], color=BOND, lw=w, solid_capstyle="round", zorder=z, alpha=0.92)

# 全分子で原子半径を統一 (長さ L はボンド長のみに反映 → ball-and-stick 風で統一感)
rO_FIX, rC_FIX, rH_FIX = 0.42, 0.36, 0.25

def co2(cx, cy, L, ang, z=10):
    """CO2 ロッド: 長さ L(O-O). 原子半径は固定 → letter 間で粒サイズ統一"""
    a = np.deg2rad(ang)
    ox, oy = np.cos(a)*L/2, np.sin(a)*L/2
    bond(cx-ox, cy-oy, cx+ox, cy+oy, z, w=rC_FIX*11)
    atom(cx-ox, cy-oy, rO_FIX, O_COL, z+1)
    atom(cx+ox, cy+oy, rO_FIX, O_COL, z+1)
    atom(cx, cy, rC_FIX, C_COL, z+3)

def water(cx, cy, ang, z=30):
    """H2O コネクタ: bisector = ang 方向. 原子半径は固定"""
    a = np.deg2rad(ang); half = np.deg2rad(104.5/2); OH = 0.72
    hs = [(cx+np.cos(a+sgn*half)*OH, cy+np.sin(a+sgn*half)*OH) for sgn in (+1,-1)]
    for hx,hy in hs: bond(cx,cy,hx,hy,z,w=rH_FIX*11)
    for hx,hy in hs: atom(hx,hy,rH_FIX,H_COL,z+1)
    atom(cx,cy,rO_FIX,O_COL,z+3)

# ============ T (左, 2 CO2 + 1 H2O) ============
# 横バー: 水平 CO2 (最上部)
co2(2.75, 7.35, L=2.7, ang=0,  z=10)
# 縦棒: 垂直 CO2 (バー直下 → 下端)
co2(2.75, 4.45, L=4.0, ang=90, z=20)   # O が y=6.45 と 2.45
# 分岐点(バーと縦棒の接点)に H2O
water(2.75, 6.9, ang=270, z=40)

# ============ K (右, 4 CO2 + 1 H2O) ============
xK = 5.5
# 縦棒: 垂直 CO2 ×2 (上下). 内側 O をハブから1本分離す
co2(xK, 6.7, L=1.6, ang=90, z=10)    # 上 (O: 7.5, 5.9)
co2(xK, 3.3, L=1.6, ang=90, z=10)    # 下 (O: 4.1, 2.5)
# 分岐点 H2O ハブ: 中央, H を斜め方向(±52°)へ向ける = 斜め線の起点
water(xK, 5.0, ang=0, z=40)
# 斜め: 水の H の先から伸ばす (内側 O が独立して見える)
co2(6.9, 6.81, L=1.7, ang=52,  z=14)    # 上斜め (O: 6.38,6.14 / 7.43,7.48)
co2(6.9, 3.19, L=1.7, ang=-52, z=14)    # 下斜め

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.savefig("images/profile.png", dpi=100, facecolor=BG_OUT, pad_inches=0)
plt.close()
print("saved images/profile.png (minimal: T=2 CO2, K=4 CO2, H2O joints)")
