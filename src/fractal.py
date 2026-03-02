import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class Fractal(ABC):
    def __init__(self):
        """Abstract Base Class (ABC), so cannot be used on its own.
        """
        self.point_list = []

    @property
    @abstractmethod
    def color(self):
        """How to color the fractal if color is selected
        """

    @abstractmethod
    def _starting_point(self) -> np.ndarray:
        """Defines the point from which iteration begins.
        """

    @abstractmethod
    def _update_rule(self, old_x: np.ndarray, discard_point: bool = False) -> np.ndarray:
        """Defines how to compute the next point from the current point."""

    def _finalize_iteration(self) -> None:
        """Hook for subclasses to post-process stored iteration data."""
        self.point_list = np.array(self.point_list)

    def iterate(self, steps: int, discard: int = 0) -> None:
        """Find points iteratively using the subclass update rule.

        Args:
            steps (int): Number of points to store.
            discard (int, optional): Number of initial points to generate but discard.
        """
        # TODO: add safeguards so we don't accidentally iterate twice in the same object?
        old_x = self._starting_point()

        for _ in range(discard):
            old_x = self._update_rule(old_x, discard_point=True)

        for _ in range(steps):
            old_x = self._update_rule(old_x)
            self.point_list.append(old_x)

        self._finalize_iteration()

    def plot(self, color: bool = False):
        """Plots the fractal.

        Args:
            color (bool, optional): Whether or not to plot in color. Defaults to False.
        """
        if color == False:
            plt.scatter(*zip(*self.point_list), s=0.05, c="black")
        elif type(self.color) == str:
            plt.scatter(*zip(*self.point_list), s=0.05, c=self.color)
        else:
            plt.scatter(*zip(*self.point_list), s=0.05, c=self.color, cmap="gist_ncar")

        plt.axis("equal")
        plt.axis("off")

    def show(self, color: bool = False):
        """Displays plot.

        Args:
            color (bool, optional): Whether or not to plot in color. Defaults to False.
        """
        self.plot(color)
        plt.show()

    def savepng(self, outfile: str, color: bool = False):
        """Saves a PNG of the plot.

        Args:
            outfile (str): Desired filename as a string. If specified, the file extension must be .png.
            color (bool, optional): Whether or not to plot in color. Defaults to False.

        Raises:
            ValueError: Occurs if filename is specified with an extension other than .png.
        """
        self.plot(color)

        # Testing filename conditions
        dotindex = outfile.find(".")
        if dotindex == -1:
            plt.savefig(f"{outfile}.png", dpi=300)
            plt.close()
        elif outfile.lower().endswith((".png")):
            plt.savefig(f"{outfile}", dpi=300)
            plt.close()
        else:
            raise ValueError("File extension not supported.")

