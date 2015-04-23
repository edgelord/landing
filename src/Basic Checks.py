# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:09:40 2015

@author: Jordan
"""
import numpy as np
import math

step = 1
r = 7.25
max_ang_level = 5


def get_safe_angle_positions(positions, grid):    
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
    
if __name__ == "__main__": 
    grid = np.random.rand(500, 500)*2
    positions = list()
    for x in np.arange(8.5, grid.shape[0]-8.5-1, step):
        for y in np.arange(8.5, grid.shape[1]-8.5-1, step):
            positions.append((x,y))
        
    get_safe_angle_positions(positions, grid)