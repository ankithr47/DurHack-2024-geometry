import matplotlib.pyplot as plt
import numpy as np
x_list = []
y_list = []

while True:
    coords = input("enter coordinates (enter 'q' to break): ").split(',')
    if coords == ['q']:
        break
    x_list.append(int(coords[0]))
    y_list.append(int(coords[1]))

plt.scatter(x_list, y_list)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.show()
