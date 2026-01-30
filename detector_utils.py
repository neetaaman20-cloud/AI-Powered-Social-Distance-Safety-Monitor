import numpy as np
from scipy.spatial import distance as dist

def calculate_distance(p1, p2):
    return dist.euclidean(p1, p2)

def get_center(bbox):
    xmin, ymin, xmax, ymax = bbox
    return (int((xmin + xmax) / 2), int((ymin + ymax) / 2))