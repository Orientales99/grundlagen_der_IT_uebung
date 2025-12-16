import simpy


class ProductionMaterial:
    def __init__(self, env: simpy.Environment, name: str, initial_quantity: int,
                 capacity: int):
        self.env: simpy.Environment = env
        self.name: str = name

        # init: Menge an Material welches gerade zur Verfügung steht
        # capacity: Maximale Menge die in dem Container gespeichert werden kann
        self.container: simpy.Container = simpy.Container(self.env,
                                                          init= initial_quantity,
                                                          capacity=capacity)


    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Quantity in Container: {self.container.level}")
        print(f"Capacity in Container: {self.container.capacity}")



env = simpy.Environment()

mehl = ProductionMaterial(env, "Mehl", 5, 100)

mehl.print_details()