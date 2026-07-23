from tyre import Tyre
soft_tyre = Tyre("Soft", 90.0, 0.15)
for lap in range(1,6):
    print(f"Lap {lap}: {soft_tyre.get_lap_time():.2f} seconds")
    soft_tyre.complete_lap()