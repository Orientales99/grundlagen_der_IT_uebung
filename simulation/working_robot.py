import simpy

from simulation.production_entity import ProductionEntity


class WorkingRobot(ProductionEntity):
    def __init__(self, env: simpy.Environment, name: str, number_of_working_robots: int):
        super().__init__(env, name, number_of_working_robots)


