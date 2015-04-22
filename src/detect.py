#!/usr/bin/python
import numpy as np
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


surf = load_file("../resources/surface1.dem")

def pix_norm(mtx, pixel):
    x, y = pixel;
    x_scl = x * .2
    y_scl = y * .2

    neighbors = [np.array ([nx*.2, ny*.2,mtx[nx, ny]])
                 for nx in [x+1, x-1] for ny in [y+1,y-1]]

    origin = np.array ([x_scl,y_scl,mtx[x,y]])
    dvec = [nbr - origin for nbr in neighbors]

    return neighbors, origin, dvec

time1 = time();
print "time 1: " + str()
v2 = np.array([8.901320,0.1021312,3.0980])
v1 = np.array([8.901320,0.1081312,7.0980])
np.cross(v1,v2)
# [np.cross(v1,v2) for x in range(500*500*4)]
time2 = time();
print "time 2: " + str(time1 - time2)


    
def lel():
    return [[[x, y] for x in range(1,498,1)] for y in range(1,498,1)]
