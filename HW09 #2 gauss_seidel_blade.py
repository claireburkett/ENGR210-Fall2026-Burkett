"""Gauss-Seidel finite-difference model of a cooled turbine blade.

Run: python gauss_seidel_blade.py
Requires numpy and matplotlib. Saves blade_temperature.png beside this file.

The pictured geometry is periodic: 6 mm channel width + 4 mm gap. Use symmetry
to solve only half a pitch (5 mm), from a channel centerline to the midpoint
between channels. The blade is 6 mm thick; each channel is 2 mm high and
centered, leaving 2 mm of solid above and below. Both outer faces are exposed
to combustion gas. Channel walls are exposed to the cooling air.

The grid is cell-centred and the five-point steady conduction equation is
solved by point Gauss-Seidel. Convection is applied as a face heat flux; this
is the finite-volume form of the finite-difference control-volume balance.
"""

import numpy as np
import matplotlib.pyplot as plt

# Properties and operating conditions (SI units)
k = 25.0                 # W/(m K)
h_hot, T_hot = 1000.0, 1700.0  # W/(m² K), K
h_air, T_air = 200.0, 400.0    # W/(m² K), K

# Symmetry reduces the repeating 10 mm pitch (6 mm channel + 4 mm spacing)
# to a 5 mm half-pitch, from a channel centerline to the midpoint of the gap.
Lx, Ly = 5e-3, 6e-3
channel_x_end = 3e-3    # half of the 6 mm channel width
channel_y0, channel_y1 = 2e-3, 4e-3
dx = dy = 0.10e-3       # 0.10 mm grid; channel edges align with grid
nx, ny = round(Lx / dx), round(Ly / dy)
tol = 1e-3              # K maximum point update
max_iter = 100000


def solve():
    x = (np.arange(nx) + 0.5) * dx
    y = (np.arange(ny) + 0.5) * dy
    # True denotes solid metal. The passage occupies x=0..3 mm, y=2..4 mm.
    air = ((x[:, None] < channel_x_end) &
           (y[None, :] >= channel_y0) & (y[None, :] < channel_y1))
    solid = ~air
    T = np.full((nx, ny), 1000.0)
    T[air] = T_air

    # Face conductances per metre of channel length. Internal solid-solid
    # faces conduct; solid-air faces convect; the top/bottom faces see hot gas.
    gx, gy = k * dy / dx, k * dx / dy
    hx, hy = h_air * dy, h_air * dx
    aP = np.zeros((nx, ny))
    b = np.zeros((nx, ny))
    # For each neighbor direction, (di,dj, conduction conductance, area-based
    # channel conductance). Outer x faces are symmetry and have zero flux.
    directions = ((1, 0, gx, hx), (-1, 0, gx, hx),
                  (0, 1, gy, hy), (0, -1, gy, hy))

    for i in range(nx):
        for j in range(ny):
            if not solid[i, j]:
                continue
            for di, dj, g_cond, g_air in directions:
                ii, jj = i + di, j + dj
                if ii < 0 or ii >= nx:  # symmetry planes
                    continue
                if jj < 0 or jj >= ny:
                    # Outer hot-gas face. Include half-cell conduction
                    # resistance in series with convection resistance.
                    g = 1.0 / (dy / (2.0 * k * dx) + 1.0 / (h_hot * dx))
                    aP[i, j] += g
                    b[i, j] += g * T_hot
                elif not solid[ii, jj]:
                    aP[i, j] += g_air
                    b[i, j] += g_air * T_air
                else:
                    aP[i, j] += g_cond

    for iteration in range(1, max_iter + 1):
        largest_change = 0.0
        for i in range(nx):
            for j in range(ny):
                if not solid[i, j]:
                    continue
                rhs = b[i, j]
                for di, dj, g_cond, _ in directions:
                    ii, jj = i + di, j + dj
                    if (0 <= ii < nx and 0 <= jj < ny and solid[ii, jj]):
                        rhs += g_cond * T[ii, jj]
                updated = rhs / aP[i, j]
                largest_change = max(largest_change, abs(updated - T[i, j]))
                T[i, j] = updated
        if largest_change < tol:
            break
    else:
        raise RuntimeError("Gauss-Seidel failed to converge; increase max_iter.")

    # Reconstruct one complete 10 mm pitch by reflecting the half-cell about
    # its inter-channel symmetry boundary. Reverse x so the channel appears at
    # both ends of the repeated pitch.
    T_full = np.concatenate((T, T[::-1, :]), axis=0)
    solid_full = np.concatenate((solid, solid[::-1, :]), axis=0)
    x_full = (np.arange(2 * nx) + 0.5) * dx
    hottest = np.unravel_index(np.argmax(np.where(solid_full, T_full, -np.inf)), T_full.shape)

    # Heat entering from the two combustion-gas faces, per metre of channel.
    g_hot = 1.0 / (dy / (2.0 * k * dx) + 1.0 / (h_hot * dx))
    q_hot_per_length = sum(
        g_hot * (T_hot - T[i, j])
        for i in range(nx) for j in (0, ny - 1) if solid[i, j]
    )
    # Half-pitch result covers half of the 10 mm repeating pitch; double it.
    q_hot_per_length *= 2.0

    print(f"Converged in {iteration} iterations; largest update {largest_change:.2e} K")
    print(f"Maximum metal temperature: {T_full[hottest]:.2f} K")
    print(f"Location in repeated 10 mm pitch: x={x_full[hottest[0]]*1e3:.2f} mm, "
          f"y={y[hottest[1]]*1e3:.2f} mm")
    print(f"Heat from combustion gas per metre of channel: {q_hot_per_length:.2f} W/m")

    # Display the cavity in white and the solid as a temperature heat map.
    masked = np.ma.masked_where(~solid_full.T, T_full.T)
    cmap = plt.colormaps["inferno"].copy()
    cmap.set_bad("white")
    fig, ax = plt.subplots(figsize=(10, 4.3), constrained_layout=True)
    im = ax.imshow(masked.T, origin="lower", extent=(0, 10, 0, 6),
                   aspect="equal", cmap=cmap, interpolation="nearest")
    fig.colorbar(im, ax=ax, label="Temperature (K)")
    ax.set(title="Turbine blade temperature (symmetric 10 mm repeat cell)",
           xlabel="Distance across channels (mm)", ylabel="Blade thickness (mm)")
    ax.set_aspect("equal")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    plt.show()
    return T_full, solid_full


if __name__ == "__main__":
    solve()
