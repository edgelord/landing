import numpy as np

def pauls_shit(surf):
    X = np.array([[x*.2 for x in range(500)] for y in range(500)]).flatten()
    Y = np.array([[y*.2 for x in range(500)] for y in range(500)]).flatten()
    Z = np.array([[surf[x,y] for x in range(500)] for y in range(500)]).flatten()
    return np.array ([X, Y, Z])
