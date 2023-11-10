def closest_pair(points):
    # Base case: If there are only a few points, use brute force
    if len(points) <= 3:
        return brute_force_closest_pair(points)

    # Step 1: Sort points based on x-coordinates
    sorted_points = sort_points_by_x(points)

    # Step 2: Divide
    mid = len(sorted_points) // 2
    left_half = sorted_points[:mid]
    right_half = sorted_points[mid:]

    # Step 3: Recursively Solve
    left_closest_pair = closest_pair(left_half)
    right_closest_pair = closest_pair(right_half)

    # Step 4: Merge
    min_dist_pair = merge(left_half, right_half, min(left_closest_pair, right_closest_pair))

    # Step 5: Select Minimum
    return min_dist_pair

import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_point_to_starting_point(points, starting_point):
    # Sort points based on distance from the starting point
    sorted_points = sorted(points, key=lambda p: distance(p, starting_point))

    # Find the minimum distance and corresponding point
    min_distance = float('inf')
    closest_point = None

    for i in range(1, len(sorted_points)):
        current_distance = distance(sorted_points[i], starting_point)
        if current_distance < min_distance:
            min_distance = current_distance
            closest_point = sorted_points[i]

    return closest_point

