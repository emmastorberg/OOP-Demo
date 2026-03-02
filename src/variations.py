import numpy as np
import matplotlib.pyplot as plt

from typing import Self

from fractal import Fractal
from chaos_game import ChaosGame
from barnsley_fern import BarnsleyFern


class Variations:
    eps = 1e-12

    def __init__(self, x: np.ndarray, y: np.ndarray, name: str):
        self.x = x
        self.y = y
        self.name = name
        self._func = getattr(Variations, self.name)

    def transform(self):
        return self._func(self.x, self.y)

    @classmethod
    def from_fractal(cls, fractal: Fractal, name: str) -> Self:
        """Create a specific variation of a fractal.
        Args:
            fractal (Fractal): Fractal instance containing generated points
            name (str): Name of transformation function to apply

        Returns:
            Self: Variations instance initialized with point data extracted from Fractal object
        """
        x = fractal.point_list[:, 0]
        y = fractal.point_list[:, 1]
        warp = cls(x, y, name)
        return warp

    # ----------------------- TRANSFORMATIONS ------------------- #

    """
    All the static methods take in pairs of x- and y-values, and they return
    the values after transforming them as defined in the appendix of this
    document: https://flam3.com/flame_draves.pdf

    Skipped all dependent/parametric transformations.
    """

    # Variation 0
    @staticmethod
    def linear(x, y):
        return x, -y

    # Variation 1
    @staticmethod
    def sinusoidal(x, y):
        return np.sin(x), np.sin(y)

    # Variation 2
    @staticmethod
    def spherical(x, y):
        r2 = x**2 + y**2 + Variations.eps
        return x / r2, y / r2

    # Variation 3
    @staticmethod
    def swirl(x, y):
        r = np.sqrt(x**2 + y**2)
        return x * np.sin(r**2) - y * np.cos(r**2), x * np.cos(r**2) + y * np.sin(r**2)

    # Variation 4
    @staticmethod
    def horseshoe(x, y):
        r = np.sqrt(x**2 + y**2) + Variations.eps
        return (x - y) * (x + y) / r, (2 * x * y) / r

    # Variation 5
    @staticmethod
    def polar(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return theta / np.pi, r - 1

    # Variation 6
    @staticmethod
    def handkerchief(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return r * np.sin(theta + r), r * np.cos(theta - r)

    # Variation 7
    @staticmethod
    def heart(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return r * np.sin(theta * r), -r * np.cos(theta * r)

    # Variation 8
    @staticmethod
    def disc(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return (theta / np.pi) * np.sin(np.pi * r), (theta / np.pi) * np.cos(np.pi * r)

    # Variation 9
    @staticmethod
    def spiral(x, y):
        r = np.sqrt(x**2 + y**2) + Variations.eps
        theta = np.arctan2(x, y)
        return (np.cos(theta) + np.sin(r)) / r, (np.sin(theta) - np.cos(r)) / r

    # Variation 10
    @staticmethod
    def hyperbolic(x, y):
        r = np.sqrt(x**2 + y**2) + Variations.eps
        theta = np.arctan2(x, y)
        return np.sin(theta) / r, r * np.cos(theta)

    # Variation 11
    @staticmethod
    def diamond(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return np.sin(theta) * np.cos(r), np.cos(theta) * np.sin(r)

    # Variation 12
    @staticmethod
    def ex(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        p0 = np.sin(theta + r)
        p1 = np.cos(theta - r)
        return r * (p0**3 + p1**3), r * (p0**3 - p1**3)

    # Variation 13
    @staticmethod
    def julia(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        omega = np.random.randint(0, 2, size=x.shape) * np.pi
        return np.sqrt(r) * np.cos(theta / 2 + omega), np.sqrt(r) * np.sin(
            theta / 2 + omega
        )

    # Variation 14
    @staticmethod
    @np.vectorize
    def bent(x, y):
        if x >= 0 and y >= 0:
            return x, y
        if x < 0 and y >= 0:
            return 2 * x, y
        if x >= 0 and y < 0:
            return x, 0.5 * y
        if x < 0 and y < 0:
            return 2 * x, 0.5 * y

    # Variation 16
    @staticmethod
    def fisheye(x, y):
        r = np.sqrt(x**2 + y**2)
        factor = 2 / (r + 1 + Variations.eps)
        return factor * y, factor * x

    # Variation 18
    @staticmethod
    def exponential(x, y):
        return np.exp(x - 1) * np.cos(np.pi * y), np.exp(x - 1) * np.sin(np.pi * y)

    # Variation 19
    @staticmethod
    def power(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return r ** np.sin(theta) * np.cos(theta), r ** np.sin(theta) * np.sin(theta)

    # Variation 20
    @staticmethod
    def cosine(x, y):
        return np.cos(np.pi * x) * np.cosh(y), -np.sin(np.pi * x) * np.sinh(y)

    # Variation 27
    @staticmethod
    def eyefish(x, y):
        r = np.sqrt(x**2 + y**2)
        return 2 * x / (r + 1 + Variations.eps), 2 * y / (r + 1 + Variations.eps)

    # Variation 28
    @staticmethod
    def bubble(x, y):
        r2 = x**2 + y**2
        return 4 * x / (r2 + 4), 4 * y / (r2 + 4)

    # Variation 29
    @staticmethod
    def cylinder(x, y):
        return np.sin(x), y

    # Variation 31
    @staticmethod
    def noise(x, y):
        psi1 = np.random.uniform(0, 1, size=x.shape)
        psi2 = np.random.uniform(0, 1, size=x.shape)
        return psi1 * x * np.cos(2 * np.pi * psi2), psi1 * y * np.sin(2 * np.pi * psi2)

    # Variation 34
    @staticmethod
    def blur(x, y):
        psi1 = np.random.uniform(0, 1, size=x.shape)
        psi2 = np.random.uniform(0, 1, size=x.shape)
        return psi1 * np.cos(2 * np.pi * psi2), psi1 * np.sin(2 * np.pi * psi2)

    # Variation 35
    @staticmethod
    def gaussian(x, y):
        sum = 0
        for i in range(4):
            psi = np.random.uniform(0, 1, size=x.shape)
            sum += psi
        factor = sum - 2
        psi = np.random.uniform(0, 1, size=x.shape)
        return factor * x * np.cos(2 * np.pi * psi), factor * y * np.sin(
            2 * np.pi * psi
        )

    # Variation 42
    @staticmethod
    def tangent(x, y):
        return np.sin(x) / np.cos(y), np.tan(y)

    # Variation 43
    @staticmethod
    def square(x, y):
        psi1 = np.random.uniform(0, 1, size=x.shape)
        psi2 = np.random.uniform(0, 1, size=x.shape)
        return psi1 - 0.5, psi2 - 0.5

    # Variation 48
    @staticmethod
    def cross(x, y):
        factor = np.sqrt(1 / (x**2 - y**2 + Variations.eps) ** 2)
        return factor * x, factor * y


# ----------------------- NOT IN CLASS ----------------------- #


def linear_combination_wrap(v1: Fractal, v2: Fractal) -> callable:
    """Defines and returns a function "weighted".

    Args:
        v1 (Variations): Variation of a fractal plot
        v2 (Variations): Variation of a fractal plot

    Returns:
        callable: Returns a method for calculating the linear combination the Variations v1 and v2.
    """

    def weighted(w: float) -> tuple[np.ndarray, np.ndarray]:
        """Performs addition and scaling of transformed fractal plots (of Variations type) v1 and v2 by some scalar.

        Args:
            w (float): Scalar in the interval [0,1]

        Returns:
            tuple[np.ndarray, np.ndarray]: New grid containing variations v1 and v2 linearly combined by the scalar w.
        """
        x1, y1 = v1.transform()
        x2, y2 = v2.transform()
        X = w * x2 + (1 - w) * x1
        Y = w * y2 + (1 - w) * y1
        return X, Y

    return weighted


if __name__ == "__main__":
    # Making transformation catalog figure, showing all possible transformations ----------
    grid_values = np.linspace(-1, 1, 170)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()

    transformations = [
        "linear",
        "sinusoidal",
        "spherical",
        "swirl",
        "horseshoe",
        "polar",
        "handkerchief",
        "heart",
        "disc",
        "spiral",
        "hyperbolic",
        "diamond",
        "ex",
        "julia",
        "bent",
        "fisheye",
        "exponential",
        "power",
        "cosine",
        "eyefish",
        "bubble",
        "cylinder",
        "noise",
        "blur",
        "gaussian",
        "tangent",
        "square",
        "cross",
    ]
    variations = [
        Variations(x_values, y_values, version) for version in transformations
    ]

    fig, axs = plt.subplots(7, 4, figsize=(16, 28))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        u, v = variation.transform()
        ax.scatter(u, -v, s=0.2, marker=".", color="black")
        ax.set_title(variation.name)
        ax.axis("equal")
        ax.axis("off")
    fig.savefig("figures/transformation_catalog.png")

    # Making warped fractal plots ---------------------------------------------------------
    # ChaosGame:
    ngon = ChaosGame(5, 5 / 8)
    ngon.iterate(20000)

    transformations = ["linear", "swirl", "handkerchief", "polar", "bent", "horseshoe"]
    variations = [
        Variations.from_fractal(ngon, version) for version in transformations
    ]

    fig, axs = plt.subplots(3, 2, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        u, v = variation.transform()
        ax.scatter(u, -v, s=0.2, marker=".", c=ngon.color, cmap="gist_ncar")
        ax.set_title(variation.name)
        ax.axis("equal")
        ax.axis("off")
    fig.savefig("figures/warped_chaos_game.png")

    # BarnsleyFern:
    fern = BarnsleyFern()
    fern.iterate(50000)

    transformations = ["linear", "power", "ex", "julia", "diamond", "fisheye"]
    variations = [
        Variations.from_fractal(fern, version) for version in transformations
    ]

    fig, axs = plt.subplots(3, 2, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        u, v = variation.transform()
        ax.scatter(u, -v, s=0.2, marker=".", c=fern.color)
        ax.set_title(variation.name)
        ax.axis("equal")
        ax.axis("off")
    fig.savefig("figures/warped_barnsley_fern.png")

    # Making linear combinations of warped ChaosGame plots ------------------------------------
    ngon = ChaosGame(4, 0.48)
    ngon.iterate(30000)
    colors = ngon.color

    coeffs = np.linspace(0, 1, 4)

    variation1 = Variations.from_fractal(ngon, "linear")
    variation2 = Variations.from_fractal(ngon, "exponential")

    variation1and2combo = linear_combination_wrap(variation1, variation2)

    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for ax, w in zip(axs.flatten(), coeffs):
        u, v = variation1and2combo(w)

        ax.scatter(u, -v, s=0.2, marker=".", c=colors, cmap="cool")
        ax.set_title(f"weight = {w:.2f}")
        ax.axis("off")
    fig.savefig("figures/linear_combination.png")
