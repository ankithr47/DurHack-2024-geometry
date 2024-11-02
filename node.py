import math
class node:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distanceFrom(self,node2):
        return math.sqrt((node2.x - self.x)**2+(node2.y - self.y)**2)
    def distanceList(nodelist):
        totalDistance = 0
        for i in range(0,len(nodelist)):
            totalDistance += nodelist[i].distanceFrom(nodelist[(i+1)%len(nodelist)])
        return totalDistance
    def area(xlist,ylist):
        nodelist = []
        for i in range(0,len(xlist)):
            nodelist.append(node(xlist[i],ylist[i]))
        node0 = nodelist[0]
        node1 = nodelist[1]
        node2 = nodelist[2]
        node3 = nodelist[3]
        d1 = distanceList([node0,node1,node2,node3])
        
                


