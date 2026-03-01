![Tests](https://github.com/emmastorberg/OOP-Demo/actions/workflows/test.yml/badge.svg)

# Object-Oriented Programming Demo
Demonstration of object-oriented principles for KDA

## About the program
In the Chaos Game, we build fractals point by point within n-gons. We select a random starting point in the interior of the shape, and with a few random selections of vertices and placing points down according to a specific ruleset, we produce a fractal pattern over many iterations. This procedure is carried out in the program `chaos_game.py`, and lets us create figures such as these for various values of $n$:

[![Chaos Game art with n = 3, i.e. a triangle. See figures/ for more plots.](figures/chaos1.png)](figures/chaos1.png)

The program `variations.py` specifies a number of 2D transformations, displayed in terms of their effect on a grid below:

[![Possible transformations shown on a grid.](figures/transformation_catalog.png)](figures/transformation_catalog.png)

We can apply these transformations to our Chaos Game plots as well:

[![Warped Chaos Game plots](figures/warped_chaos_game.png)](figures/warped_chaos_game.png)

We can even make linear combinations of various transformations to combine different warpings, or to change the intensity of the effect:

[![Linear combinations of the linear (no warp) and exponential transformation as the exponential weight increases](figures/linear_combination.png)](figures/linear_combination.png)

## How to run
Create Chaos Game plots by running:

``uv run chaos_game.py``

Generate the transformation catalog and warped Chaos Game plots by running:

``uv run variations.py``

Run simple tests with:

``uv run pytest``

## Helpful sources
The math and algorithm behind the Chaos Game (and a few more variants of it) is described in detail [here](https://thewessens.net/ClassroomApps/Main/chaosgame.html). The definitions of the various transformation functions were found in the appendix of [this paper](https://flam3.com/flame_draves.pdf).
