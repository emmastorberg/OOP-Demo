import numpy as np
import matplotlib.pyplot as plt
from utils import random_point

class ChaosGame:
    def __init__(self):
        ...

    def _starting_point(self) -> np.ndarray:
        """Selects a random point within the n-gon.

        Returns:
            np.ndarray: Random point in the interior of the shape
        """
        return random_point(self.corners)