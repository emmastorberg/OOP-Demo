import numpy as np
import matplotlib.pyplot as plt


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
