from utils.distances import euclidean

def test_euclidean():
    assert euclidean((0, 0), (0, 0)) == 0
    assert euclidean((0, 0), (3, 4)) == 5
    assert euclidean((0, 0), (1, 0)) == 1
    assert euclidean((0, 0), (0, 1)) == 1
    assert euclidean((0, 0), (-1, 0)) == 1
    assert euclidean((0, 0), (0, -1)) == 1
    assert euclidean((0, 0), (-3, -4)) == 5
    assert euclidean((0, 0), (3, -4)) == 5
    assert euclidean((0, 0), (-3, 4)) == 5
