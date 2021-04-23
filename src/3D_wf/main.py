import pyglet
import wired
import projection

piramide = wired.WireFrame()

piramide.addNode(100,100,0)
piramide.addNode(200,100,0)
piramide.addNode(100,100,100)
piramide.addNode(200,100,100)
piramide.addNode(150,150,50)

piramide.addEdge(piramide.nodes[0], piramide.nodes[1])
piramide.addEdge(piramide.nodes[0], piramide.nodes[2])
piramide.addEdge(piramide.nodes[1], piramide.nodes[3])
piramide.addEdge(piramide.nodes[2], piramide.nodes[3])

piramide.addEdge(piramide.nodes[0], piramide.nodes[4])
piramide.addEdge(piramide.nodes[1], piramide.nodes[4])
piramide.addEdge(piramide.nodes[2], piramide.nodes[4])
piramide.addEdge(piramide.nodes[3], piramide.nodes[4])

pv = projection.ProjectViewer(piramide)
pv.display()
window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.RIGHT:
        piramide.transladar(10, 0, 0)
    elif symbol == pyglet.window.key.F:
        pv.visao = "frontal"
    elif symbol == pyglet.window.key.S:
        pv.visao = "superior"

    pv.display()

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    pv.batch.draw()

pyglet.app.run()