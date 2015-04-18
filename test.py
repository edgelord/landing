#!/usr/bin/python
import numpy as np
fileName = "surface1.dem"
print a[4,5]

kek = 1
# todo figure out norms relative to flat plane
def load_file(file_name):
    with open(fileName, "rb") as f:
        arrayName = np.fromfile(f, np.float32)
        arrayName.byteswap(True)
        return np.array(np.split(arrayName,500))


# l = [x for x in a]
# print l
