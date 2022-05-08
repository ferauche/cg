import pyglet
import wired

class ProjectViewer(object):
    def __init__(self, obj3d : wired.WireFrame):
        self.wf = obj3d
        self.batch = pyglet.graphics.Batch()
        self.vertex = []
        self.visao = "frontal"
        self.fep = [1, 1, 1]

    def display(self):
        if len(self.vertex) != 0:
            for vertex_list in self.vertex:
                vertex_list.delete()
            self.vertex.clear()

        pc = self.wf.center()

        for edge in self.wf.edges:
            if self.visao == "frontal":
                x1 = (edge.start.x - pc[0]) * self.fep[0] + pc[0]
                y1 = (edge.start.y - pc[1]) * self.fep[0] + pc[1]

                x2 = (edge.stop.x - pc[0]) * self.fep[0] + pc[0]
                y2 = (edge.stop.y - pc[1]) * self.fep[0] + pc[1]

            elif self.visao == "superior":
                x1 = (edge.start.x - pc[0]) * self.fep[1] + pc[0]
                y1 = (edge.start.z - pc[2]) * self.fep[1] + pc[2]

                x2 = (edge.stop.x - pc[0]) * self.fep[1] + pc[0]
                y2 = (edge.stop.z - pc[2]) * self.fep[1] + pc[2]

            elif self.visao == "lateral":
                x1 = (edge.start.z - pc[2]) * self.fep[2] + pc[2]
                y1 = (edge.start.y - pc[1]) * self.fep[2] + pc[1]

                x2 = (edge.stop.z - pc[2]) * self.fep[2] + pc[2]
                y2 = (edge.stop.y - pc[1]) * self.fep[2] + pc[1]

            self.vertex.append(self.batch.add(2, pyglet.gl.GL_LINES, None, ('v2i', (int(x1), int(y1), int(x2), int(y2)))))
        print(self.visao)
        self.wf.show_nodes()



