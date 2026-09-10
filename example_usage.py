from client import SPHFluidSimulator

def main():
    print("=== Testing SPH Particle Hydrodynamics ===")
    sph = SPHFluidSimulator(h=1.0, rest_density=0.1, gas_const=1000.0)

    particles = [(0.0, 0.0), (0.2, 0.0), (0.0, 0.2), (-0.2, 0.0)]
    density, pressure = sph.compute_density_pressure(particles, target_idx=0)

    print(f"Target particle density: {round(density, 4)}, pressure: {round(pressure, 4)}")
    assert density > 0.0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
