from utils.distances import manhattan

def test_manhattan():
    assert manhattan((0, 0), (0, 0)) == 0
    assert manhattan((0, 0), (1, 1)) == 2
    assert manhattan((0, 0), (1, 0)) == 1
    assert manhattan((0, 0), (0, 1)) == 1
    assert manhattan((0, 0), (-1, 0)) == 1
    assert manhattan((0, 0), (0, -1)) == 1
    assert manhattan((0, 0), (-1, -1)) == 2
    assert manhattan((0, 0), (1, -1)) == 2
    assert manhattan((0, 0), (-1, 1)) == 2
