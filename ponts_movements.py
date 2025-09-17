def points_movement_tracker(points):
    res = 0                      # Initialize total movement cost
    x1, y1 = points.pop()        # Start from the last point

    while points:                # While there are more points
        x2, y2 = points.pop()    # Get the next point (from the end)
        res += max(abs(x1 - x2), abs(y1 - y2))  # Add Chebyshev distance
        x1, y1 = x2, y2          # Update current point
    return res                   # Return total movement cost
