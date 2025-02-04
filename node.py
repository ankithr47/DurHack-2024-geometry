import math
from itertools import permutations
import shapely.geometry

# create a class for each vertex of the shape
class node:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # method to find distance between 2 nodes(vertices)
    def distanceFrom(self,other):
        return math.sqrt((other.x - self.x)**2+(other.y - self.y)**2)
    
    # method to calculate total distance between a given path of 4 nodes
    # answer depends on list order 
    def total_distance(nodelist):
        totalDistance = 0
        for i in range(len(nodelist)):
            totalDistance += nodelist[i].distanceFrom(nodelist[(i+1)%len(nodelist)]) #wrap around
        return totalDistance
    
    ''' method to reorder the coordinates such that drawing a line between each 
        coordinate in the new order will produce the quadrilateral'''
    def order(xlist,ylist ):
        # create nodes from given coordinates
        nodes = [node(x,y) for x, y in zip(xlist, ylist)]
            
        # generate all permutations of nodes
        node_permutations = permutations(nodes)

        # find permutation with smallest total distance
        min_distance = float('inf')
        best_order = None

        for i in node_permutations:
            distance = node.total_distance(i)
            if distance < min_distance:
                min_distance = distance
                best_order = i

        # extract ordered x and y coordinates
        order_x = [node.x for node in best_order]
        order_y = [node.y for node in best_order]

        return order_x, order_y
    
    # method to find area of quadrilateral
    def area(xlist,ylist):
        # convert xlist and ylist into a single list of coordinates (nodelist)
        nodelist = []
        for i in range(0,len(xlist)):
            nodelist.append(node(xlist[i],ylist[i]))
        # split quadrilateral into 2 triangles and use Heron's formula to compute the area of each triangle
        s1 = node.total_distance([nodelist[0],nodelist[1],nodelist[2]])/2   # s1 = semiperimeter of triangle 1
        s2 = node.total_distance([nodelist[0],nodelist[3],nodelist[2]])/2   # s2 = semiperimeter of triangle 2 
        a1 = math.sqrt(s1*(s1-nodelist[0].distanceFrom(nodelist[1]))*(s1-nodelist[1].distanceFrom(nodelist[2]))*(s1-nodelist[2].distanceFrom(nodelist[0]))) # a1 = area of triangle 1
        a2 = math.sqrt(s2*(s2-nodelist[0].distanceFrom(nodelist[3]))*(s2-nodelist[3].distanceFrom(nodelist[2]))*(s2-nodelist[2].distanceFrom(nodelist[0]))) # a2 = area of triangle 2
        return a1 + a2
    
    def efficient_order(xlist, ylist):
        '''this method is more efficient than order,
        as it has O(nlogn) whereas order has O(n!)'''
        # Calculate the centroid of the points
        centroid_x = sum(xlist) / len(xlist)
        centroid_y = sum(ylist) / len(ylist)
        
        # Compute the angle of each point relative to the centroid
        points = list(zip(xlist, ylist))
        angles = [
            math.atan2(y - centroid_y, x - centroid_x) for x, y in points
        ]
        
        # Sort points based on the angles in counterclockwise order
        sorted_points = sorted(zip(points, angles), key=lambda item: item[1])
        
        # Unpack the sorted points into x and y lists
        ordered_points = [p for p, angle in sorted_points]
        ordered_x, ordered_y = zip(*ordered_points)
        
        return list(ordered_x), list(ordered_y)

    '''Function below doesn't quite work yet. The aim is to find the area
    of any regular/irregular polygon by splitting it up into triangles
    (via an algorithm shown on polygonareapseudo.txt) and computing the area of each triangle using Heron's formula'''

    def total_area(xlist, ylist):
        # create list of x, y nodes
        nodes = [node(x,y) for x,y in zip(xlist, ylist)]
        # create polygon
        polypoints =[(xlist[i], ylist[i]) for i in range(len(xlist))]
        polygon = shapely.geometry.Polygon(polypoints)
        i = 0
        tot_area = 0
        while len(nodes) > 3:
            test_coord = shapely.geometry.Point((nodes[i % len(nodes)].x + nodes[(i+2) % len(nodes)].x)/2, (nodes[i % len(nodes)].y + nodes[(i+2) % len(nodes)].y)/2)
            # check if test coordinate is inside the polygon, if so, find area of the triangle
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

    
    def total_area_shoelace(xlist, ylist):
        #create list of vertices
        vertices = [node(x,y) for x,y in zip(xlist, ylist)]
        vertices.append(vertices[0])
        #use shoelace theorem
        #calculate left sum
        lsum = 0
        for i in range(len(vertices)-1):
            lsum += (vertices[i].x *vertices[i+1].y)
        #calculate right sum
        rsum = 0
        for j in range(len(vertices)-1):
            rsum += (vertices[j].y *vertices[j+1].x)
        
        total = 0.5 * abs(lsum - rsum)
        return total



    

    
    












