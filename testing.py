import shapely.geometry
xlist = [0, 0, 2, 2]
ylist = [0, 2, 2, 0]
points = [(xlist[i], ylist[i]) for i in range(len(xlist))]

polygon = shapely.geometry.Polygon(points)

print(polygon)

test_point = shapely.geometry.Point(1, 1)
print(test_point.within(polygon))