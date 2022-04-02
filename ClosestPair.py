import random


def dist(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5


def brute(points):
    d = 1e20
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = min(d, dist(points[i], points[j]))
    return d


def solve(x_sorted, y_sorted):
    n = len(x_sorted)
    if n <= 3:
        return brute(x_sorted)
    mid_point = x_sorted[n//2]
    x_sorted_left = x_sorted[:n//2]
    x_sorted_right = x_sorted[n//2:]

    y_sorted_left, y_sorted_right = [], []

    for point in y_sorted:
        if point[0] <= mid_point[0]:
            y_sorted_left.append(point)
        else:
            y_sorted_right.append(point)

    delta = min(solve(x_sorted_left, y_sorted_left), solve(x_sorted_right, y_sorted_right))

    strip = []
    for point in y_sorted:
        if mid_point[0]-delta < point[0] < mid_point[0]+delta:
            strip.append(point)
    d = delta
    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip)):
            d = min(d, dist(strip[i], strip[j]))

    return d


def generate_plane(plane_size, num_pts):

    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i % plane_size[0] + 1, i//plane_size[1] + 1)
                     for i in gen]

    return random_points


if __name__ == "__main__":
    num_pts = 10
    plane_size = (100, 100)
    points = generate_plane(plane_size, num_pts)
    print(points)
    print(brute(points))
    x_sorted = sorted(points, key=lambda x: x[0])
    y_sorted = sorted(points, key=lambda y: y[1])
    print(solve(x_sorted, y_sorted))
