import math
import random


def dist(p1, p2):

    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5


#!========================================================================================================================
def sort_points_by_X(points):

    return sorted(points)
#!==========================================================================================================================


def sort_points_by_Y(points):

    return sorted(points, key=lambda Y: Y[1])

#!=========================================================================================================================


def naive_closest_pair(plane):  # ? Brute Force Apporach
    min_dis = float('inf')
    for i in range(len(plane)):
        for j in range(i+1, len(plane)):
            d = dist(plane[i], plane[j])
            if d < min_dis:
                min_dis = d
                point1 = plane[i]
                point2 = plane[j]

    return [min_dis, point1, point2]

#!============================================DIVIDE AND CONQUER================================================================================


def closest_pair_in_strip(points, d):
    min_dis = d
    P = sort_points_by_Y(points)
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            if abs(P[j][1]-P[i][1]) < min_dis:
                if dist(P[i], P[j]) < min_dis:
                    min_dis = dist(P[i], P[j])
                    point1 = P[i]
                    point2 = P[j]
    if min_dis < d:
        return [min_dis, point1, point2]
    else:
        return -1


#!=================================================================================================================================

def efficient_closest_pair_routine(points):
    if len(points) <= 3:
        return naive_closest_pair(points)

    points = sort_points_by_X(points)
    mid = len(points)//2
    midPoint = points[mid]
    P_L = points[:mid]
    P_R = points[mid:]

    global point1, point2

    dl = efficient_closest_pair_routine(P_L)
    dr = efficient_closest_pair_routine(P_R)
    L = []
    d = min(dl, dr)

    for i in range(len(points)):

        if (points[i][0]-midPoint[0]) < d[0]:
            L.append(points[i])

    D = closest_pair_in_strip(L, d[0])
    if D == -1:
        return naive_closest_pair(plane)
    else:
        return min(d, D)

#!======================================================================================================================================================


def efficient_closest_pair(points):
    P = sort_points_by_X(points)
    return efficient_closest_pair_routine(P)
#!==========================================================================================================================


def generate_plane(plane_size, num_pts):

    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i % plane_size[0] + 1, i//plane_size[1] + 1)
                     for i in gen]

    return random_points

#!========================================================================================================


if __name__ == "__main__":
    num_pts = 10
    plane_size = (10, 10)
    plane = generate_plane(plane_size, num_pts)
    print(plane)
    print(efficient_closest_pair(plane))
    print(naive_closest_pair(plane))

# ?note:  change the num_pts or plane_size to see the difference in time-complexity of both method
