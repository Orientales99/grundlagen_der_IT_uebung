import simpy

from src.machine import Machine
from src.working_robot import WorkingRobot
from src.production_material import ProductionMaterial
from src.monitoring import Monitoring

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
working_robot = WorkingRobot(env, "Teig_wr", 2)


# Materialien
machine_schokoladenueberzug = Machine(env, "Schokoladenueberzug_ma", 1, working_robot,False, heisse_schokolade, kalte_schokolade,
                                      production_time=1)
machine_teig = Machine(env, "Teig_ma", 1,working_robot,  True, teig, wasser, mehl, 2)
machine_lebkuchen = Machine(env, "Lebkuchen_ma", 1, working_robot,  True, marzipan, heisse_schokolade, teig, 1)

# Monitoring instanziieren
monitor = Monitoring(env, product_list)

# Starte Produktionsprozesse
machine_schokoladenueberzug.start_production()
machine_teig.start_production()
machine_lebkuchen.start_production()

env.process(monitor.monitoring_process())


env.run(until=100)
monitor.plot_results()