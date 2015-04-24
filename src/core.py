# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:09:40 2015

@author: luber2
"""
import numpy as np
import math
import weak_elimination
import detect
import platform

step = 1
r = 7.25
max_ang_level = 4

resource_dir = "../resources/"
data = resource_dir+"dem.dat"

def main(filename):
    print(filename)
    print(platform.system())
    if platform.system() == "Windows":
        filename.replace("/", "\\")
    grid = detect.load_file(filename)
    print(grid)
    pos_grid = get_pos_grid(grid)
    #pos_grid = weak_elimination.lv1_elimination(grid, pos_grid)
    
    valid_pos, norms = get_safe_angle_positions_and_norms(get_pos_from_pos_grid(pos_grid), grid)
    
    result_grid = np.zeros(grid.shape[0], grid.shape[1])
    for p in valid_pos:
        for x in range(math.floor(p[0]-8.5), math.ceil(p[0]+8.5)):
            for y in range(math.floor(p[1]-8.5), math.ceil(p[1]+8.5)):
                result_grid[x][y] = 255
                
    return result_grid
        
def get_pos_grid(grid):
    pos_grid = np.ones((grid.shape[0]-17)/step, (grid.shape[1]-17)/step)
    return pos_grid
    
    
def get_pos_from_pos_grid(grid):    
    positions = list()
    for x in np.arange(8.5, grid.shape[0]-8.5-1, step):
        for y in np.arange(8.5, grid.shape[1]-8.5-1, step):
            positions.append((x,y))


def get_safe_angle_positions_and_norms(positions, grid):    
    valid_pos = list()
    valid_norms = list()
    for pos in positions:
        x = pos[0]
        y = pos[1]           
        points = dict()
        lv = 0
        while lv <= max_ang_level:
            get_point_dict(points, lv)
            lv+=1
        norms = get_norms(points, x, y, grid)
        
        if check_angles(norms):
            valid_pos.append(pos)
            valid_norms.append(norms)
            
    return (valid_pos, valid_norms)


def get_point_dict(points, lv):
    if len(points) == 0:
        points[0] = ([r, 0])
        return
    newpoints = dict()
    for a in points.keys():
        new_a = a + (90/math.pow(2, lv))
        newpoints[new_a] = ([(r*np.cos(math.radians(new_a))), (r*np.sin(math.radians(new_a)))])
    points.update(newpoints)
        
def get_norms(points, x, y, grid):
    norms = dict()
    for a in points.keys():
        p = points[a]
        tlp = get_tl(p, x, y, grid)
        trp = get_tr(p, x, y, grid)
        blp = get_bl(p, x, y, grid)
        brp = get_br(p, x, y, grid)       
        
        tlnorm = get_unit_vector(np.cross(trp - tlp, blp - tlp))
        trnorm = get_unit_vector(np.cross(brp - trp, tlp - trp))
        blnorm = get_unit_vector(np.cross(tlp - blp, brp - blp))
        brnorm = get_unit_vector(np.cross(blp - brp, trp - brp))
        
        
        norms[a] = (tlnorm, trnorm, blnorm, brnorm)
        
        
    return norms
        
def get_tl(p, x, y, grid):
    tempx = x - p[1]
    tempy = y + p[0]
    return np.array([tempx, tempy, get_height(tempx, tempy, grid)])
    
def get_tr(p, x, y, grid):
    tempx = x + p[0]
    tempy = y + p[1]
    return np.array([tempx, tempy, get_height(tempx, tempy, grid)])
    
def get_bl(p, x, y, grid):
    tempx = x - p[0]
    tempy = y - p[1]
    return np.array([tempx, tempy, get_height(tempx, tempy, grid)])
    
def get_br(p, x, y, grid):
    tempx = x + p[1]
    tempy = y - p[0]
    return np.array([tempx, tempy, get_height(tempx, tempy, grid)])
    
def get_height(x, y, grid):
    tr = grid[math.ceil(x)][math.ceil(y)]
    tl = grid[math.floor(x)][math.ceil(y)]
    br = grid[math.ceil(x)][math.floor(y)]
    bl = grid[math.floor(x)][math.floor(y)]
    
    a = (math.ceil(x) - x) * (math.ceil(y) - y)
    b = (x - math.floor(x)) * (math.ceil(y) - y)
    c = (math.ceil(x) - x) * (y - math.floor(y))
    d = (x - math.floor(x)) * (y - math.floor(y))
    
    return (a*tr) + (b*tl) + (c*br) + (d*bl)
    
    
def check_angles(norms):
    flat = np.array([0,0,1])
    #print(norms)
    for a in norms.keys():
        for normal_vector in norms[a]:
            #print(normal_vector)
            angle = get_angle(flat, normal_vector)     
            #print(math.degrees(angle)%180)
            if (math.degrees(angle)%180 >= 10.2) and (math.degrees(angle)%180 <= 169.8):
                return False
    return True
            
def get_unit_vector(vector):
    return vector / np.linalg.norm(vector)
            
def get_angle(v1, v2):
    angle = np.arccos(np.dot(v1, v2))
    if np.isnan(angle):
        if (v1 == v2).all():
            return 0.0
        else:
            return np.pi
    return angle
    
def load_dem(file_name):
    with open(file_name, "rb") as f:
        array = np.fromfile(f, np.float32)
        array.byteswap(True)
        return np.reshape(array,(500,500))

def main():
    # grid = load_dem("../resources/surface2.dem")
    grid = np.random.rand(500, 500)*2
    positions = list()
    for x in np.arange(8.5, grid.shape[0]-8.5-1, step):
        for y in np.arange(8.5, grid.shape[1]-8.5-1, step):
            positions.append((x,y))
        
<<<<<<< HEAD
    get_safe_angle_positions(positions, grid)
    
if __name__ == "__main__": 
    main()
=======
    get_safe_angle_positions_and_norms(positions, grid)
>>>>>>> 9406d8eb6d43939b8b92fa8858fd6a629ee3cda4
