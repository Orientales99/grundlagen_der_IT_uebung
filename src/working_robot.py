import simpy

from src.production_robot import ProductionRobot


class WorkingRobot(ProductionRobot):
    def __init__(self, env: simpy.Environment, name: str, number_of_working_robots: int):
        super().__init__(env, name, number_of_working_robots)


