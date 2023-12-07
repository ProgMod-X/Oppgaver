import math
import random

N = 10000000
r = 2
sum_of_lengths = 0


def gen_two_rnd_points(r):
    angle1 = random.uniform(0, 2 * math.pi)
    angle2 = random.uniform(0, 2 * math.pi)

    x1 = r * math.cos(angle1)
    y1 = r * math.sin(angle1)

    x2 = r * math.cos(angle2)
    y2 = r * math.sin(angle2)

    return (x1, y1), (x2, y2)


def calc_length_between_two_points(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


for i in range(N):
    points = gen_two_rnd_points(r)
    length = calc_length_between_two_points(points[0], points[1])
    sum_of_lengths += length

print(f"Den gjennomsnittlige avstanden mellom to punkt på en sirkel er {round(sum_of_lengths/N, 2)} med radius {r}")