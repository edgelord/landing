#!/usr/bin/python
import numpy as np
import numpy.linalg as la

rsc = "../resources/"
s1 = rsc + "surface1.dem"
s2 = rsc + "surface2.dem"

p = 1

# todo figure out norms relative to flat plane
def load_file(file_name):
    with open(file_name, "rb") as f:
        arrayName = np.fromfile(f, np.float32)
        arrayName.byteswap(True)
        return np.array(np.split(arrayName,500))


surf = load_file("../resources/surface2.dem")

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


    
def lel():
    return [[[x, y] for x in range(1,498,1)] for y in range(1,498,1)]
