import simpy

from simulation.machine import Machine
from simulation.working_robot import WorkingRobot
from simulation.production_material import ProductionMaterial
from simulation.monitoring import Monitoring

env = simpy.Environment()

# Produkte
# Rohmaterial
mehl = ProductionMaterial(env, "Mehl", 50, 100)
wasser = ProductionMaterial(env, "Wasser", 50, 100)
kalte_schokolade = ProductionMaterial(env, "Kalte Schokolade", 10, 100)

# Zwischenprodukte
heisse_schokolade = ProductionMaterial(env, "Heisse Schokolade", 0, 100)
teig = ProductionMaterial(env, "Teig", 0, 100)

# Endprodukt
marzipan = ProductionMaterial(env, "Lebkuchen", 0, 100)

# liste aus allen Produkten
product_list: list[ProductionMaterial] = [mehl, wasser, kalte_schokolade,heisse_schokolade, teig, marzipan]

# Working_Robots
working_robot = WorkingRobot(env, "Working_Robot", 2)


# Maschine
machine_schokoladenueberzug = Machine(env, "Schokoladenueberzug_ma", 1,False, heisse_schokolade, kalte_schokolade,
                                      production_time=150, working_robots=working_robot)
machine_teig = Machine(env, "Teig_ma", 1,  True, teig, wasser, mehl, 3, working_robot)
machine_lebkuchen = Machine(env, "Lebkuchen_ma", 1,  True, marzipan, heisse_schokolade, teig, 60, working_robot)

# Monitoring instanziieren
monitor = Monitoring(env, product_list)

# Starte Produktionsprozesse
machine_schokoladenueberzug.start_production()
machine_teig.start_production()
machine_lebkuchen.start_production()

env.process(monitor.monitoring_process())

env.run(until=1000)
monitor.plot_results()