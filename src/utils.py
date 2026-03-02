import numpy as np

# -------------------- HELPER CLASS FOR DEFINING BARNSLEY FERN --------------------
class AffineTransform:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y) -> np.ndarray:
        """
        Defines a transformation with the matrix multiplication and addition by a constant vector. The matrix and constant vector are defined in the constructor when the class is instantiated, and when it is called, it
        takes an x- and y-value as an initial condition.
        """
        x_new = self.a * x + self.b * y + self.e
        y_new = self.c * x + self.d * y + self.f
        return np.array([x_new, y_new])
    

# ------------------- HELPER METHODS FOR DEFINING CHAOS GAME ------------------------

def random_point(corners: list[np.ndarray]) -> np.ndarray:
    """Finds a random point within an n-gon.

    Args:
        corners (list[np.ndarray]): List of arrays corresponding to the corner coordinates of the n-gon.

    Returns:
        np.ndarray: Randomly selected point in the interior of the n-gon.
    """
    n = len(corners)
    # Finding random weights
    weights_list = np.array(np.zeros(n))
    for i in range(n):
        weights_list[i] = np.random.random()

    # Normalizing weights
    sum = np.sum(weights_list)
    for i in range(n):
        weights_list[i] = weights_list[i] / sum

    # Creating point from corners and normalized weights
    X = np.zeros(np.shape(corners)[1])
    for corner, weight in zip(corners, weights_list):
        X += weight * corner

    return X


def generate_ngon(n) -> list[np.ndarray]:
        """Defines corners of the n-gon based on n provided during initialization and stores corners in a list.

        Returns:
            list[np.ndarray]: List of corners as NumPy arrays.
        """
        theta = np.linspace(0, 2 * np.pi, n + 1)
        corners = []

        for i in range(n):
            corners.append(np.array([np.sin(theta[i]), np.cos(theta[i])]))

        return corners


def compute_optimal_r(n: int) -> float:
    """Calculate the optimal r value for an n-sided polygon Chaos Game.
    
    Based on the geometric formula:
    r_opt = (1 + 2a) / (2 + 2a)
    where a = sum_{i=1}^{n} cos[i(π - θ)]

    Source: https://en.wikipedia.org/wiki/Chaos_game
    
    Args:
        n (int): Number of sides of the polygon
        
    Returns:
        float: Optimal r value for the Chaos Game
    """
    # Internal angle of the polygon
    theta = (n - 2) * np.pi / n
    
    # Index of most protruding vertex
    j = int(np.floor(n / 4))
    
    # Calculate a as the sum
    a = sum(np.cos(i * (np.pi - theta)) for i in range(1, j + 1))
    
    # Calculate optimal r
    r_opt = (1 + 2 * a) / (2 + 2 * a)
    
    return round(r_opt, 3)