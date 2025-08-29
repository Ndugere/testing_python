def min_moves_possible(points):
    res = 0
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        res += max(abs(x1 - x2), abs(y1 - y2))
    return res
