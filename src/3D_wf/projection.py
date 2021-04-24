import pyglet
import wired

class ProjectViewer(object):
    def __init__(self, obj3d : wired.WireFrame):
        self.wf = obj3d
        self.batch = pyglet.graphics.Batch()
        self.vertex = []
        self.visao = "frontal"

    def display(self):
        if len(self.vertex) != 0:
            for vertex_list in self.vertex:
                vertex_list.delete()
            self.vertex.clear()

        for edge in self.wf.edges:
            if self.visao == "frontal":
                x1 = edge.start.x
                y1 = edge.start.y

                x2 = edge.stop.x
                y2 = edge.stop.y
            elif self.visao == "superior":
                x1 = edge.start.x
                y1 = edge.start.z

                x2 = edge.stop.x
                y2 = edge.stop.z

            self.vertex.append(self.batch.add(2, pyglet.gl.GL_LINES, None, ('v2i', (x1, y1, x2, y2))))




