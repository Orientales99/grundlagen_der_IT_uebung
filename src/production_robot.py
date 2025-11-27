import simpy

class ProductionRobot:
    def __init__(self, environment: simpy.Environment, name: str, number_of_entities:int = 1):
        self.env:  simpy.Environment() = environment
        self.name: str = name

        self.resource = simpy.Resource(self.env, capacity=number_of_entities)


