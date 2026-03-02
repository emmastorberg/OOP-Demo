import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from chaos_game import ChaosGame
import pytest


def test_constructor_raises_ValueError_for_small_n():
    # Checking if a ValueError is raised
    with pytest.raises(ValueError):
        line = ChaosGame(2)


@pytest.mark.parametrize("n, expected_r", [(5, 0.618), (6, 0.667), (7, 0.692), (8, 0.707), (9, 0.742), (10, 0.764)])
def test_optimal_r_is_computed(n, expected_r):
    # Checking if optimal r is found when no r is provided.
    shape = ChaosGame(n)
    assert round(shape.r, 3) == expected_r


def test_correct_amount_of_corners():
    # Checking that the n-gon has n corners
    shape = ChaosGame(6)
    assert len(shape.corners) == 6


def test_point_list_length():
    # Checking the number of points before and after iteration
    octagon = ChaosGame(8, 0.4)
    assert len(octagon.point_list) == 0

    octagon.iterate(10000)
    assert len(octagon.point_list) == 10000


def test_savepng_raises_ValueError_for_incorrect_extension():
    # Checking if a ValueError is raised
    with pytest.raises(ValueError):
        square = ChaosGame(4, 1 / 3)
        square.iterate(10000)
        square.savepng("shouldnotwork.pdf", color=True)


if __name__ == "__main__":
    test_constructor_raises_ValueError_for_small_n()
    test_optimal_r_is_computed()
    test_correct_amount_of_corners()
    test_point_list_length()
    test_savepng_raises_ValueError_for_incorrect_extension()
