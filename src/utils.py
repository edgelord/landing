import numpy as np

def pauls_shit(surf,x_range, y_range):
    x_min, x_max = x_range
    y_min, y_max = y_range
    assert x_min < x_max
    assert y_min < y_max
    X = np.array([[x*.2 for x in range(x_min, x_max, 1)] for y in range(500)]).flatten()
    Y = np.array([[y*.2 for y in range(y_min, y_max, 1)] for y in range(500)]).flatten()
    Z = np.array([[surf[x,y] for x in range(500)] for y in range(500)]).flatten()
    return np.array ([X, Y, Z])

def load_file(file_name):
    with open(file_name, "rb") as f:
        array = np.fromfile(f, np.float32)
        array.byteswap(True)
        return np.reshape(array,(500,500))

