import math

class SPHFluidSimulator:
    """
    Smoothed Particle Hydrodynamics (SPH) Density and Tait Pressure.
    Cubic spline smoothing kernel W(r, h).
    """
    def __init__(self, h=1.0, rest_density=1000.0, gas_const=2000.0):
        self.h = h
        self.rho0 = rest_density
        self.k = gas_const

    def kernel_cubic_spline(self, r):
        q = r / self.h
        sigma = 10.0 / (7.0 * math.pi * (self.h**2))
        if 0 <= q <= 1:
            return sigma * (1.0 - 1.5*(q**2) + 0.75*(q**3))
        elif 1 < q <= 2:
            return sigma * 0.25 * ((2.0 - q)**3)
        return 0.0

    def compute_density_pressure(self, particles, target_idx, mass=1.0):
        tx, ty = particles[target_idx]
        density = 0.0
        for px, py in particles:
            r = math.sqrt((tx - px)**2 + (ty - py)**2)
            density += mass * self.kernel_cubic_spline(r)
        pressure = max(0.0, self.k * (density - self.rho0))
        return density, pressure
