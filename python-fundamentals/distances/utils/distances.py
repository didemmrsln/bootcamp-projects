def minkowski(a, b, p):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]
    distance = (abs(d_x)**p + abs(d_y)**p)**(1/p)
    return distance


def manhattan(a, b):
    return minkowski(a, b, 1)


def euclidean(a, b):
    return minkowski(a, b, 2)
