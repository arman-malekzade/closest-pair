__author__ = 'Arman Malekzade'
import math
input_points = [
    [2.0, 8.0],
    [3.0, 7.0],
    [4.0, 6.0],
    [5.0, 5.0],
    [6.0, 4.0],
    [7.0, 3.0],
    [8.0, 2.0]
]


def closest_pair(points):
    if len(points) == 3:
        dist_p1_p2 = math.sqrt(math.pow(points[0][0] - points[1][0], 2) + math.pow(points[0][1] - points[1][1], 2))
        dist_p1_p3 = math.sqrt(math.pow(points[0][0] - points[2][0], 2) + math.pow(points[0][1] - points[2][1], 2))
        dist_p2_p3 = math.sqrt(math.pow(points[1][0] - points[2][0], 2) + math.pow(points[1][1] - points[2][1], 2))
        return min(dist_p1_p2, dist_p1_p3, dist_p2_p3)
    if len(points) == 2:
        dist_p1_p2 = math.sqrt(math.pow(points[0][0] - points[1][0], 2) + math.pow(points[0][1] - points[1][1], 2))
        return dist_p1_p2
    points_sorted_by_x = points[:]
    points_sorted_by_x.sort(key=lambda x: x[0])
    points_sorted_by_y = points[:]
    points_sorted_by_y.sort(key=lambda x: x[1])
    separation_line_x_coordinate = ((points_sorted_by_x[-1][0] + points_sorted_by_x[0][0]) / 2)
    first_half = []
    second_half = []
    for p in points_sorted_by_x:
        if p[0] < separation_line_x_coordinate:
            first_half.append(p)
        else:
            second_half.append(p)

    delta_left = closest_pair(first_half)
    delta_right = closest_pair(second_half)
    delta = min(delta_left, delta_right)
    for p in points_sorted_by_x:
        if abs(p[0] - separation_line_x_coordinate) > delta:
            points_sorted_by_x.remove(p)
    points_sorted_by_x.sort(key=lambda x: x[1])
    remaining_points_sorted_by_y = points_sorted_by_x[:]
    for i in range(len(remaining_points_sorted_by_y)):
        for j in range(i+1, min(i+11, len(remaining_points_sorted_by_y))):
            current_point_x = remaining_points_sorted_by_y[i][0]
            current_point_y = remaining_points_sorted_by_y[i][1]
            current_cmp_point_x = remaining_points_sorted_by_y[j][0]
            current_cmp_point_y = remaining_points_sorted_by_y[j][1]
            current_distance = math.sqrt(math.pow(current_point_x - current_cmp_point_x, 2) + math.pow(current_point_y - current_cmp_point_y, 2))
            if current_distance < delta:
                delta = current_distance
    return delta


print closest_pair(input_points)
