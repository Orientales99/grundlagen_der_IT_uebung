import simpy


class ProductionMaterial:
    def __init__(self, env: simpy.Environment, name: str, initial_quantity, capacity: int):
        self.env: simpy.Environment = env
        self.name: str = name

        # init: Menge an Material welches gerade zur Verfügung steht
        # capacity: Maximale Menge die in dem Container gespeichert werden kann
        self.container: simpy.Container = simpy.Container(self.env, init= initial_quantity, capacity=capacity)

        # Format: (zeit, produktname, bestand)
        self.history: list[tuple[float, float]] = []

    def get_material_quantity(self) -> float:
        return self.container.level

    def log_state(self):
        """Speichert aktuellen Zustand in die history-Liste."""
        self.history.append((self.env.now, self.container.level))