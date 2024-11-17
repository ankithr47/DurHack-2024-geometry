import math
from itertools import permutations
import shapely.geometry

class node:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceFrom(self,other):
        return math.sqrt((other.x - self.x)**2+(other.y - self.y)**2)
    
    def total_distance(nodelist):
        totalDistance = 0
        for i in range(len(nodelist)):
            totalDistance += nodelist[i].distanceFrom(nodelist[(i+1)%len(nodelist)]) #wrap around
        return totalDistance
    
    def order(xlist,ylist ):
        #create nodes from given coordinates
        nodes = [node(x,y) for x, y in zip(xlist, ylist)]
            
        #generate all permutations of nodes
        node_permutations = permutations(nodes)

        #find permutation with smallest total distance
        min_distance = float('inf')
        best_order = None

        for i in node_permutations:
            distance = node.total_distance(i)
            if distance < min_distance:
                min_distance = distance
                best_order = i

        #extract ordered x and y coordinates
        order_x = [node.x for node in best_order]
        order_y = [node.y for node in best_order]

        return order_x, order_y

    """
    if (d1 < d2 and d1 < d3):
        return [node0.x,node1.x,node2.x,node3.x], [node0.y,node1.y,node2.y,node3.y]
    elif (d2 < d1 and d2 < d3):
        return [node0.x,node1.x,node3.x,node2.x], [node0.y,node1.y,node3.y,node2.y]
    else:
        return [node0.x,node2.x,node1.x,node3.x], [node0.y,node2.y,node1.y,node3.y]
    """
    
    def area(xlist,ylist):
        nodelist = []
        for i in range(0,len(xlist)):
            nodelist.append(node(xlist[i],ylist[i]))
        s1 = node.total_distance([nodelist[0],nodelist[1],nodelist[2]])/2
        s2 = node.total_distance([nodelist[0],nodelist[3],nodelist[2]])/2
        p1 = math.sqrt(s1*(s1-nodelist[0].distanceFrom(nodelist[1]))*(s1-nodelist[1].distanceFrom(nodelist[2]))*(s1-nodelist[2].distanceFrom(nodelist[0])))
        p2 = math.sqrt(s2*(s2-nodelist[0].distanceFrom(nodelist[3]))*(s2-nodelist[3].distanceFrom(nodelist[2]))*(s2-nodelist[2].distanceFrom(nodelist[0])))
        return p1 + p2

    def total_area(xlist, ylist):
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









