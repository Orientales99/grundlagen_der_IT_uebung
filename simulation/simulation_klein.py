import simpy

from simulation.machine import Machine
from simulation.working_robot import WorkingRobot
from simulation.production_material import ProductionMaterial


env = simpy.Environment()

# Produkte
# Rohmaterial
mehl = ProductionMaterial(env, "Mehl", 5, 100)
wasser = ProductionMaterial(env, "Wasser", 50, 100)

#Endprodukt
teig = ProductionMaterial(env, "Teig", 0, 100)


# Working_Robots
working_robot = WorkingRobot(env, "Working_Robot", 2)

# Maschine
machine_teig = Machine(env, "Teig_ma", 1,  True, teig, wasser, mehl, 3, working_robot)

machine_teig.start_production()

env.run(until=100)
