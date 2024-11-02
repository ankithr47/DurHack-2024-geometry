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
    def order(xlist,ylist ):
        node0 = node(xlist[0],ylist[0])
        node1 = node(xlist[1],ylist[1])
        node2 = node(xlist[2],ylist[2])
        node3 = node(xlist[3],ylist[3])
        d1 = node.distanceList([node0,node1,node2,node3])
        d2 = node.distanceList([node0,node1,node3,node2])
        d3 = node.distanceList([node0,node2,node1,node3])
        if (d1 < d2 and d1 < d3):
            return [node0.x,node1.x,node2.x,node3.x], [node0.y,node1.y,node2.y,node3.y]
        elif (d2 < d1 and d2 < d3):
            return [node0.x,node1.x,node3.x,node2.x], [node0.y,node1.y,node3.y,node2.y]
        else:
            return [node0.x,node2.x,node1.x,node3.x], [node0.y,node2.y,node1.y,node3.y]
    def area(xlist,ylist):
        nodelist = []
        for i in range(0,len(xlist)):
            nodelist.append(node(xlist[i],ylist[i]))
        s1 = node.distanceList([nodelist[0],nodelist[1],nodelist[2]])
        s2 = node.distanceList([nodelist[0],nodelist[3],nodelist[2]])
        p1 = math.sqrt(s1(s1-nodelist[0].distanceFrom(nodelist[1]))(s1-nodelist[1].distanceFrom(nodelist[2]))(s1-nodelist[2].distanceFrom(nodelist[0])))
        p2 = math.sqrt(s2(s2-nodelist[0].distanceFrom(nodelist[3]))(s2-s1-nodelist[3].distanceFrom(nodelist[2]))(s2-nodelist[2].distanceFrom(nodelist[0])))
        return p1 + p2
list1, list2 = node.order([0,1,5,6],[0,5,1,4])
print(list1)
print(list2)
print(node.area(list1,list2))


