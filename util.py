from math import *
import numpy as np

# The number of degrees per meter of circumference on Earth (radius of 6.317 million meters)
# This is a suitable approximation as the low altitude of the UAV will produce negligible differences in latitude and longitude
DEGREES_PER_METER = 360 / (2 * pi * 6.317e6)

# Generate a rotation matrix around the x-axis
def matrix_rot_x(theta):
    s, c = sin(theta), cos(theta)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]])

# Generate a rotation matrix around the y-axis
def matrix_rot_y(theta):
    s, c = sin(theta), cos(theta)
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]])