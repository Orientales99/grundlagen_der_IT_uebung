import simpy

from src.production_robot import ProductionRobot
from src.production_material import ProductionMaterial
from src.working_robot import WorkingRobot


class Machine(ProductionRobot):
    def __init__(self, env: simpy.Environment, name: str, number_of_machines: int, working_robots: WorkingRobot, benoetigt_working_robot: bool, product: ProductionMaterial,
                 material_one: ProductionMaterial, material_two: ProductionMaterial | None = None, production_time: int = 1):
        super().__init__(env, name, number_of_machines)

        self.working_robots: WorkingRobot = working_robots
        self.benoetigt_working_robot: bool=benoetigt_working_robot

        self.product: ProductionMaterial = product

        self.material_one: ProductionMaterial = material_one
        self.material_two: ProductionMaterial = material_two

        self.production_time: int = production_time



        self.producing_product: bool = False

    def producing_product_process(self):
        while True:
            if self.producing_product:
                # benötigten Rohstoffe werden aus den Containern genommen, wenn vorhanden
                yield self.material_one.container.get(1)

                if self.material_two is not None:
                    yield self.material_two.container.get(1)

                # überprüfen, ob ein Working Robot benötigt wird
                if self.benoetigt_working_robot:
                    with self.working_robots.resource.request() as request:
                        yield request

                yield self.env.timeout(self.production_time)
                print(f"Produkt {self.product.name} wurde um {self.env.now} fertig gestellt")

                yield self.product.container.put(1)
            else:
                print(f"Produktion der Maschine {self.name} wurde um {self.env.now} beendet.")
                break

    # Schnittstellen
    def start_production(self):
        if self.producing_product:
            print(f"Produktion der Maschine {self.name} läuft bereits")

        else:
            self.producing_product = True
            self.env.process(self.producing_product_process())
            print(f"Produktion der Maschine {self.name} wurde um {self.env.now} gestartet.")

    def end_production_process(self):
            self.producing_product=False


