import math


class Node(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Edge(object):

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

class WireFrame(object):

    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, x, y, z):
        self.nodes.append(Node(x,y,z))

    def addEdge(self, start : Node, stop : Node):
        self.edges.append(Edge(start, stop))

    def transladar(self, tx, ty, tz):
        for node in self.nodes:
            node.x += tx
            node.y += ty
            node.z += tz

    def escalar(self, fe):
        pm = self.center()

        for node in self.nodes:
            xref = node.x - pm[0]
            yref = node.y - pm[1]
            zref = node.z - pm[2]

            node.x = xref * fe
            node.y = yref * fe
            node.z = zref * fe

            node.x += pm[0]
            node.y += pm[1]
            node.z += pm[2]

    def rotacionar(self, eixo, rad):
        pm = self.center()

        for node in self.nodes:
            if eixo == 'x':
                y = node.y - pm[1]
                z = node.z - pm[2]

                d = math.hypot(y,z)
                theta = math.atan2(y,z)

                node.z = pm[2] + d * math.cos(theta+rad)
                node.y = pm[1] + d * math.sin(theta+rad)
            elif eixo == 'y':
                x = node.x - pm[0]
                z = node.z - pm[2]

                d = math.hypot(z,x)
                theta = math.atan2(z,x)

                node.x = pm[0] + d * math.cos(theta+rad)
                node.z = pm[2] + d * math.sin(theta+rad)
            elif eixo == 'z':
                x = node.x - pm[0]
                y = node.y - pm[1]

                d = math.hypot(y,x)
                theta = math.atan2(y,x)

                node.x = pm[0] + d * math.cos(theta+rad)
                node.y = pm[1] + d * math.sin(theta+rad)

    def center(self):
        mx = 0
        my = 0
        mz = 0
        for node in self.nodes:
            mx += node.x
            my += node.y
            mz += node.z

        return [mx / len(self.nodes), my / len(self.nodes), my / len(self.nodes)]

    def show_nodes(self):
        for node in self.nodes:
            print("("+str(node.x)+", "+str(node.y)+", "+str(node.z)+")");

