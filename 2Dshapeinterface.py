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

x_new_lst, y_new_lst = node.order(x_list, y_list)


points = np.column_stack((x_new_lst, y_new_lst))
p = Polygon(points)
ax = plt.gca()

ax.add_patch(p)
ax.set_xlim(min(x_list)-1, max(x_list)+1)
ax.set_ylim(min(y_list)-1, max(y_list)+1)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.text(s=('area=', round(node.area(x_list,y_list), 2)), x=sum(x_list)/len(x_list), y=min(y_list)-0.5)
plt.show()

