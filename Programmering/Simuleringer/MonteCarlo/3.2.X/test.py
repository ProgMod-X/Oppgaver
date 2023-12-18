import math
import time
import random
from line_profiler import LineProfiler

fps = 60
width = 400
height = 400
radius = 5
r = 150
N = 1000
cases = 0


def is_outside(point1, point2, point3):
    # Check to see if point1(A) is outside the line defined by point2(B) and point3(C)
    # If the cross product is positive, point1 is outside the line

    # |BC| |[BC.x BC.y]|
    # |BA| |[BA.x BA.y]|

    cross_product = (point3[0] - point2[0]) * (point1[1] - point2[1]) - (point3[1] - point2[1]) * (point1[0] - point2[0])

    # print(cross_product)

    ##
    ##
    # Play with > or <
    ##
    ##
    return cross_product < 0


def check_angle(p1, p2, p3):
    # p1(A), p2(B), p3(C)
    # Check to see if angle BAC is less than 180 degrees

    # Calculate vectors AB and AC
    vector_AB = (p2[0] - p1[0], p2[1] - p1[1])
    vector_AC = (p3[0] - p1[0], p3[1] - p1[1])

    # Calculate dot product of vectors AB and AC
    dot_product = vector_AB[0] * vector_AC[0] + vector_AB[1] * vector_AC[1]

    if dot_product == 0:
        return False

    # Calculate lengths of vectors AB and AC
    length_AB = math.sqrt(vector_AB[0]**2 + vector_AB[1]**2)
    length_AC = math.sqrt(vector_AC[0]**2 + vector_AC[1]**2)

    # Calculate cosine of the angle between vectors AB and AC
    cosine_angle = dot_product / (length_AB * length_AC)

    # Handle numerical precision issues
    cosine_angle = max(-1.0, min(1.0, cosine_angle))

    # Calculate the angle in radians
    angle_rad = math.acos(cosine_angle)

    # Convert radians to degrees
    angle_deg = math.degrees(angle_rad)

    # Check if the angle is less than 180 degrees

    ##
    ##
    ## Play with this number, prev num 180
    ##
    ##
    
    return angle_deg < 150, angle_deg

for _ in range(N):

    points = []
    count = 0
    sum_of_angles = 0

    for i in range(5):
        point = (random.random() * width, random.random() * height)

        points.append(point)


    for i in range(5):
        check, degrees = check_angle(points[i], points[i - 1], points[i - 4])
        sum_of_angles += degrees
        if is_outside(points[i], points[i - 2], points[i - 3]) and check:
            count += 1

    points.append(points[0])


    if count == 5 and round(sum_of_angles) == 180:
        cases += 1
    # time.sleep(1/fps)

print(f"Estimated chance for 5 random points to create a valid pentagram is {round(cases/N,2) * 100}%")