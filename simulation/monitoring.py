import simpy
import matplotlib.pyplot as plt

from simulation.production_material import ProductionMaterial

class Monitoring:
    def __init__(self, env: simpy.Environment, product_list: list[ProductionMaterial]):
        self.env = env
        self.product_list: list[ProductionMaterial] = product_list



    def monitoring_process(self):
        while True:
            for product in self.product_list:
                product.log_state()
            yield self.env.timeout(0.5)


    def plot_results(self):
        """Erstellt eine Grafik mit allen Bestandsverläufen."""
        plt.figure(figsize=(10, 6))

        for product in self.product_list:
            times = [t for (t, _) in product.history]
            levels = [lvl for (_, lvl) in product.history]

            plt.plot(times, levels, label=product.name)

        plt.xlabel("Zeit")
        plt.ylabel("Bestand im Container")
        plt.title("Bestandsverlauf der Produktionsmaterialien")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()