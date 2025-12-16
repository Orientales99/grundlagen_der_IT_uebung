import simpy


class ProductionMaterial:
    def __init__(self, env: simpy.Environment, name: str, initial_quantity,
                 capacity: int):
        self.env: simpy.Environment = env
        self.name: str = name

        # init: Menge an Material welches gerade zur Verfügung steht
        # capacity: Maximale Menge die in dem Container gespeichert werden kann
        self.container: simpy.Container = simpy.Container(self.env, init=initial_quantity, capacity=capacity)

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Quantity in Container: {self.container.level}")
        print(f"Capacity in Container: {self.container.capacity}")


class ProductionEntity:
    def __init__(self, environment: simpy.Environment, name: str,
                 number_of_entities: int = 1):
        self.env = environment
        self.name = name

        self.resource = simpy.Resource(self.env, capacity=number_of_entities)


class WorkingRobot(ProductionEntity):
    def __init__(self, env: simpy.Environment, name: str,
                 number_of_working_robots: int):
        super().__init__(env, name, number_of_working_robots)


class Machine(ProductionEntity):
    def __init__(self, env: simpy.Environment, name: str, number_of_machines: int,
                 benoetigt_working_robot: bool, product: ProductionMaterial,
                 material_one: ProductionMaterial,
                 material_two: ProductionMaterial | None = None,
                 production_time: int = 1,  working_robots: WorkingRobot = None):
        super().__init__(env, name, number_of_machines)

        self.working_robots: WorkingRobot = working_robots
        self.benoetigt_wr: bool = benoetigt_working_robot

        self.product: ProductionMaterial = product

        self.material_one: ProductionMaterial = material_one
        self.material_two: ProductionMaterial = material_two

        self.production_time: int = production_time

        self.producing_product: bool = False


# Instanziieren von den Klassenobjekten
env = simpy.Environment()

working_robot = WorkingRobot(env, "Working_Robot", 2)

mehl = ProductionMaterial(env, "Mehl", 95, 100)
wasser = ProductionMaterial(env, "Wasser", 95, 100)
teig = ProductionMaterial(env, "Teig", 0, 100)

machine_teig = Machine(env, "Teig_ma", 1,
                       True, teig, wasser, mehl,
                       300,  working_robot)

mehl.print_details()
wasser.print_details()
teig.print_details()