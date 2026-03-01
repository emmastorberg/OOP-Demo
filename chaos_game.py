import numpy as np
import matplotlib.pyplot as plt
from utils import random_point

class ChaosGame:
    def __init__(self, n: int, r: float = 0.5):
        """Creates an n-gon according to parameter specifications.

        Args:
            n (int): Number of sides of the n-gon. Must be greater than 2.
            r (float, optional): Ratio used to find iterations of a random starting point within the n-gon. Must be in the interval (0,1). Defaults to 0.5.
        """
        if n < 3:
            raise ValueError("n must be at least 3.")
        self.n = n

        if r < 0 or r > 1:
            raise ValueError("r must be between 0 and 1")
        self.r = r

        self.corners = self._generate_ngon()
        self.point_list = []
        self.index_list = []

    @property
    def gradient_color(self):
        colors = []
        old_c = self.index_list[0]
        for i in range(len(self.index_list)):
            j = self.index_list[i]
            new_c = (old_c + j)/2
            colors.append(new_c)
            old_c = new_c

        return colors

    def _generate_ngon(self) -> list[np.ndarray]:
        """Defines corners of the n-gon based on n provided during initialization and stores corners in a list.

        Returns:
            list[np.ndarray]: List of corners as NumPy arrays.
        """
        theta = np.linspace(0, 2*np.pi,self.n+1)
        corners = []

        for i in range(self.n):
            corners.append(np.array([np.sin(theta[i]), np.cos(theta[i])]))

        return corners

    def _starting_point(self) -> np.ndarray:
        """Selects a random point within the n-gon.

        Returns:
            np.ndarray: Random point in the interior of the shape
        """
        return random_point(self.corners)

    def plot_ngon(self):
        """Plots the n-gon outline.
        """
        # TODO: Remove?
        # Creating x- and y-arrays
        x = np.zeros(self.n+1); y = np.zeros(self.n+1)

        for i in range(self.n):
            x[i] = self.corners[i][0]
            y[i] = self.corners[i][1]

        x[self.n] = self.corners[0][0]
        y[self.n] = self.corners[0][1]

        # Plotting and displaying
        plt.plot(x,y)
        plt.axis("equal")
        plt.axis("off")
        plt.show()

    def iterate(self, steps: int, discard: int = 5) -> tuple[np.ndarray, np.ndarray]:
        """Fills up the empty list of points and the list of indices (corresponding to which corner is selected) created in the constructor. 

        Args:
            steps (int): Number of iterations to do
            discard (int, optional): Number of initial steps to disregard. Defaults to 5.

        Returns:
            tuple[np.ndarray, np.ndarray]: Updated point and index lists, now as NumPy arrays.
        """
        # TODO change point and index lsit names to reflect type?
        # Iterating to make a pattern
        old_x = self._starting_point()
        for i in range(discard):
            j = np.random.randint(0, self.n)
            new_x = self.r*old_x + (1-self.r)*self.corners[j]
            old_x = new_x

        for i in range(steps):
            j = np.random.randint(0, self.n)
            new_x = self.r*old_x + (1-self.r)*self.corners[j]
            self.point_list.append(new_x)
            self.index_list.append(j)
            old_x = new_x

        self.point_list = np.array(self.point_list)     #is it weird that these are arrays now?
        self.index_list = np.array(self.index_list)

        return self.point_list, self.index_list
    
    def plot(self, color: bool = False, cmap: str = "cool"):
        """Plots the n-gon filled with points.

        Args:
            color (bool, optional): Whether or not to plot in color. Defaults to False.
            cmap (str, optional): Color map specification based on MatPlotLib presets (https://matplotlib.org/stable/gallery/color/colormap_reference.html). Defaults to "cool".
        """
        # TODO: Add warning if user specifies a color map while color bool is still set to False.
        # Testing color input
        if color == False:
            colors = "black"
        else:
            # TODO: Add handling for color
            colors = self.gradient_color

        # Plotting
        plt.scatter(*zip(*self.point_list), s=0.1, c=colors, cmap=cmap)
        plt.axis("equal")
        plt.axis("off")

    def show(self, color: bool = False, cmap: str = "cool"):
        """Displays plot.

        Args:
            color (bool, optional): Whether or not to plot in color. Defaults to False.
            cmap (str, optional): Color map specification based on MatPlotLib presets (https://matplotlib.org/stable/gallery/color/colormap_reference.html). Defaults to "cool".
        """
        self.plot(color, cmap)
        plt.show()

    def savepng(self, outfile: str, color: bool = False, cmap: str = "cool"):
        """Saves a PNG of the plot.

        Args:
            outfile (str): Desired filename as a string. If specified, the file extension must be .png.
            color (bool, optional): Whether or not to plot in color. Defaults to False.
            cmap (str, optional): Color map specification based on MatPlotLib presets (https://matplotlib.org/stable/gallery/color/colormap_reference.html). Defaults to "cool".

        Raises:
            ValueError: Occurs if filename is specified with an extension other than .png.
        """
        self.plot(color,cmap)

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
        
if __name__ == "__main__": 
    n_list = [3, 4, 5, 5, 6, 8]
    r_list = [1/2, 1/3, 1/3, 3/8, 1/3, 1/4]

    for n,r,i in zip(n_list,r_list,range(1,7)):
        shape = ChaosGame(n,r)
        shape.iterate(15000)
        shape.savepng(f"figures/chaos{i}.png",color=True)
