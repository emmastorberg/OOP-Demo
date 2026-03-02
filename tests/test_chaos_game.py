from chaos_game import ChaosGame
import pytest


def test_constructor_raises_ValueError_for_small_n():
    # Checkin if a ValueError is raised
    with pytest.raises(ValueError):
        line = ChaosGame(2)


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
    test_correct_amount_of_corners()
    test_point_list_length()
    test_savepng_raises_ValueError_for_incorrect_extension()
