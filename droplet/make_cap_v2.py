import numpy as np

# ---- EDIT THESE for your actual droplet/domain ----
R          = 0.003      # contact radius [m]
theta_deg  = 45.0        # contact angle [deg]
y_thick    = 0.00005625  # domain thickness in y (from your blockMeshDict)
n_circ     = 2360         # points around the FULL circle (increase for smoother arc)
overhang_y = 0.00001     # how far the extrusion pokes past y bounds each side
outfile    = "dropletCap.stl"
# ----------------------------------------------------

theta = np.radians(theta_deg)
a   = R * np.sin(theta)
zc  = -R * np.cos(theta)   # circle centre height (can be +/- of substrate)

phi = np.linspace(0, 2*np.pi, n_circ, endpoint=False)
xs  = R * np.cos(phi)
zs  = zc + R * np.sin(phi)
n   = n_circ

y0 = -overhang_y
y1 = y_thick + overhang_y

pts0 = np.column_stack([xs, np.full_like(xs, y0), zs])
pts1 = np.column_stack([xs, np.full_like(xs, y1), zs])

triangles = []

def tri(p1, p2, p3):
    normal = np.cross(p2 - p1, p3 - p1)
    norm = np.linalg.norm(normal)
    normal = normal / norm if norm > 0 else np.array([0, 0, 1])
    triangles.append((normal, p1, p2, p3))

# Lateral (cylindrical) surface
for i in range(n):
    j = (i + 1) % n
    tri(pts0[i], pts0[j], pts1[i])
    tri(pts0[j], pts1[j], pts1[i])

# End caps: plain fan triangulation from the circle centre — trivial and
# robust since a circle has no concave corners.
c0 = np.array([0.0, y0, zc])
c1 = np.array([0.0, y1, zc])
for i in range(n):
    j = (i + 1) % n
    tri(c0, pts0[j], pts0[i])   # winding reversed vs back cap
    tri(c1, pts1[i], pts1[j])

with open(outfile, "w") as f:
    f.write("solid dropletCap\n")
    for normal, p1, p2, p3 in triangles:
        f.write(f"  facet normal {normal[0]:.6e} {normal[1]:.6e} {normal[2]:.6e}\n")
        f.write("    outer loop\n")
        for p in (p1, p2, p3):
            f.write(f"      vertex {p[0]:.6e} {p[1]:.6e} {p[2]:.6e}\n")
        f.write("    endloop\n")
        f.write("  endfacet\n")
    f.write("endsolid dropletCap\n")

print(f"Wrote {len(triangles)} triangles to {outfile}")
print(f"a={a:.6f} m, circle centre z={zc:.6f} m")
print(f"Portion above z=0 is your cap; below z=0 is discarded automatically.")
