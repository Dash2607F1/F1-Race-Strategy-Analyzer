class Tyre:
    def __init__(self, compound, base_lap_time, degradation_per_lap):
        self.compound = compound
        self.base_lap_time = base_lap_time
        self.degradation_per_lap = degradation_per_lap
        self.laps_used = 0
    def get_lap_time(self):
        return self.base_lap_time + (self.laps_used * self.degradation_per_lap)
    def complete_lap(self):
        self.laps_used += 1
