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

