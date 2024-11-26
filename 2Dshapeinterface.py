import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from node import *

x_list = []
y_list = []
#take 4 coordinates from the user
count = 0
while count < 4:
    coords = input("enter coordinates: ").split(',')
    x_list.append(int(coords[0]))
    y_list.append(int(coords[1]))
    count += 1

# order coordinates so that a quadrilateral can be drawn between the points
x_new_lst, y_new_lst = node.order(x_list, y_list)

# create the shape from the points
points = np.column_stack((x_new_lst, y_new_lst))
p = Polygon(points)
ax = plt.gca()

# draw the shape on the axes
ax.add_patch(p)

# set limit for the numbers displayed on the x and y axis
ax.set_xlim(min(x_list)-1, max(x_list)+1)
ax.set_ylim(min(y_list)-1, max(y_list)+1)

# draw the x and y axes on the graph
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")

# display the (text showing the area) underneath the shape
plt.text(x=sum(x_list)/len(x_list), y=min(y_list)-0.5, s=(f'area = {round(node.area(x_list,y_list), 2)}'))
# show the plot
plt.show()

