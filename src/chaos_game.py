import numpy as np

from utils import random_point, generate_ngon, compute_optimal_r
from fractal import Fractal

class ChaosGame(Fractal):
    def __init__(self, n: int, r: float | None = None):
        """Creates an n-gon according to parameter specifications.

        Args:
            n (int): Number of sides of the n-gon. Must be greater than 2.
            r (float, optional): Ratio used to find iterations of a random starting point within the n-gon. Must be in the interval (0,1). Defaults to None such that optimal r-value is calculated.
        """
        super().__init__()

        if n < 3:
            raise ValueError("n must be at least 3.")
        self.n = n

        if r == None:
            r = compute_optimal_r(self.n)
        if r < 0 or r > 1:
            raise ValueError("r must be between 0 and 1")
        self.r = r

        self.corners = generate_ngon(self.n)
        self.index_list = []

    @property
    def color(self):
        colors = []
        old_c = self.index_list[0]
        for i in range(len(self.index_list)):
            j = self.index_list[i]
            new_c = (old_c + j) / 2
            colors.append(new_c)
            old_c = new_c

        return colors

    def _starting_point(self) -> np.ndarray:
        """Selects a random point within the n-gon.

        Returns:
            np.ndarray: Random point in the interior of the shape
        """
        return random_point(self.corners)
    
    def _update_rule(self, old_x: np.ndarray, discard_point: bool = False) -> np.ndarray:
        """The update rule determining the next point to place.

        Args:
            old_x (np.ndarray): The previously chosen point

        Returns:
            np.ndarray: The next point in the iteration sequence
        """
        j = np.random.randint(0, self.n)
        
        new_x = (1 - self.r) * old_x + self.r * self.corners[j]
        if not discard_point:
            self.index_list.append(j)
        
        return new_x

    def _finalize_iteration(self) -> None:
        """Post-processing data, in this case converting index_list to np.ndarray.
        """
        super()._finalize_iteration()
        self.index_list = np.array(self.index_list)


if __name__ == "__main__":
    n_list = [3, 4, 5, 5, 6, 8]
    r_list = [1 / 2, None, 0.5, None, 7/8, None]

    for n, r, i in zip(n_list, r_list, range(1, 7)):
        shape = ChaosGame(n, r)
        shape.iterate(30000, 100)
        shape.savepng(f"figures/chaos{i}.png", color=True)
