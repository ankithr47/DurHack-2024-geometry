from node import *


def total_area(xlist, ylist):
        node.order(xlist, ylist)
        #create list of x, y nodes
        nodes = [node(x,y) for x,y in zip(xlist, ylist)]
        #create polygon
        polypoints =[(xlist[i], ylist[i]) for i in range(len(xlist))]
        polygon = shapely.geometry.Polygon(polypoints)
        i = 0
        tot_area = 0
        while len(nodes) > 3:
            test_coord = shapely.geometry.Point((nodes[i % len(nodes)].x + nodes[(i+2) % len(nodes)].x)/2, nodes[i % len(nodes)].y + nodes[(i+2) % len(nodes)].y/2)
            #check if test coordinate is inside the polygon, if so, find area of the triangle
            if test_coord.within(polygon):
                s = node.total_distance([nodes[i % len(nodes)], nodes[(i+1) % len(nodes)], nodes[(i+2) % len(nodes)]]) / 2
                area = math.sqrt(s*(s-nodes[i % len(nodes)].distanceFrom(nodes[(i+1) % len(nodes)]))*(s-nodes[(i+1) % len(nodes)].distanceFrom(nodes[(i+2) % len(nodes)]))*(s-nodes[(i+2) % len(nodes)].distanceFrom(nodes[i % len(nodes)])))
                tot_area += area
                nodes.pop((i+1) % len(nodes))
                i = (i+1) % len(nodes)
            else:
                i = (i+1) % len(nodes)
        s1 = node.total_distance([nodes[0],nodes[1],nodes[2]])/2
        last_triangle_area = math.sqrt(s1*(s1-nodes[0].distanceFrom(nodes[1]))*(s1-nodes[1].distanceFrom(nodes[2]))*(s1-nodes[2].distanceFrom(nodes[0])))
        tot_area += last_triangle_area
        return tot_area

xlist = [1, 4, -2, -5]
ylist = [2, 3, 4, 5]

print(total_area(xlist, ylist))
