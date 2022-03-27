import random
import numpy as np


class Neuron:
    def __init__(self):
        self.weight = None
        self.Cwidth = 100
        self.Cheight = 100

    def weight_init(self):
        self.weight = np.array(
            [[(random.uniform(-0.3, 0.3)) for y in range(self.Cwidth)] for x in range(self.Cheight)]).flatten()
        return self.weight

    def recognize(self):
        pass

    def train(self):
        pass

    def save_w(self):
        pass

