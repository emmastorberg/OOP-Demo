import numpy as np

from utils import AffineTransform
from fractal import Fractal

class BarnsleyFern(Fractal):
    def __init__(self):
        super().__init__()
        f1 = AffineTransform(d=0.16)
        f2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.6)
        f3 = AffineTransform(0.2, -0.26, 0.23, 0.22, 0, 1.6)
        f4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)

        self.functions = [f1, f2, f3, f4]
        self.p_cumulative = [0.01, 0.86, 0.93, 1.0]

    @property
    def color(self):
        return "forestgreen"

    def _starting_point(self) -> np.ndarray:
        return np.array([0.0, 0.0]) # can be chosen freely, but (0,0) is nice to center the plot
    
    def _update_rule(self, old_x: np.ndarray, discard_point: bool = False) -> np.ndarray:
        r = np.random.random()
        for j, p in enumerate(self.p_cumulative):
            if r < p:
                F = self.functions[j]
                break

        new_x = F(old_x[0], old_x[1])
        return new_x
    

if __name__ == "__main__":
    fern = BarnsleyFern()
    fern.iterate(30000)
    fern.savepng("figures/barnsley_fern.png", True)