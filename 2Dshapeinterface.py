import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from node import *

x_list = []
y_list = []


while True:
    coords = input("enter coordinates (enter 'q' to break): ").split(',')
    if coords == ['q']:
        break
    x_list.append(int(coords[0]))
    y_list.append(int(coords[1]))

points = np.column_stack((x_list, y_list))
p = Polygon(points)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(min(x_list)-1, max(x_list)+1)
ax.set_ylim(min(y_list)-1, max(y_list)+1)
plt.show()
