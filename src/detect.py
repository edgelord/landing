#!/usr/bin/python
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import math 

resource_dir = "../resources/"
data = resource_dir+"dem.dat"

# todo figure out norms relative to flat plane
def load_file(file_name):
    with open(file_name, "rb") as f:
        array = np.fromfile(f, np.float32)
        array.byteswap(True)
        return np.reshape(array,(500,500))

surf = load_file("../resources/surface1.dem")
surf2 = load_file(resource_dir + 
surf4 = load_file("../resources/surface2.dem")

def py_ang(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    return np.arctan2(sinang, cosang)

def pix_norm(mtx, pixel):
    x, y = pixel;
    x_scl = x * .2
    y_scl = y * .2

    # trying to get neighboring pxls for norms
    neighbors = [np.array ([nbrx*.2, nbry*.2,mtx[nbrx, nbry]])
                 for nbrx, nbry in [[x+1, y], [x-1, y]]]

    # getting mid pxl val
    origin = np.array ([x_scl,y_scl,mtx[x,y]])
    v1, v3, v2, v4 = [nbr - origin for nbr in neighbors]
    n1 = np.cross(v1,v2)
    print n1
    n2 = np.cross(v3,v4)

    z = [0,0,1]
    a1 = py_ang(n1,z)
    a2 = py_ang(n2,z)
    return (a1+a2)/2

def safe_slope_mtx(surf_mtx):
    # The max derivative that is within a 10 degree incline
    max_d = 0.1763269807

    rows, cols = surf_mtx.shape
    max_mtx = [[max_d for _ in range(rows)] for _ in range(cols)]
    map_scl = [[.1 for _ in range(rows)] for _ in range(cols)]

    gx, gy = np.gradient(surf_mtx, map_scl, map_scl)

    x_safe = np.less(gx, max_mtx)
    y_safe = np.less(gy, max_mtx)
    safe_pts = np.logical_and(x_safe, y_safe)

    return safe_pts

def safe_to_pval(safe):
    if safe:
        return 255
    else: return 0


def lel():
    return [[[x, y] for x in range(1,498,1)] for y in range(1,498,1)]

M = [[1, 2, 3, 4],
     [2, 3, 4, 5],
     [4 ,6 , 8,10],
     [11,12,13,15],
     [7, 7, 7,  7]]
