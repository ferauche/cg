import pyglet
import math

# vertices da forma
forma = [(100, 100), (100, 200), (200, 100)]
batch = pyglet.graphics.Batch()
vertices = [] #armazena o vertex_list

# desenha o poligono desenhando as retas
def draw_poligon(forma2D):
    #apaga a lista de vertices da forma desenhada
    if len(vertices) != 0:
        for vertex_list in vertices:
            vertex_list.delete()
        vertices.clear()

    #indica os vertices das retas que formam o poligono
    for i in range(0, len(forma2D)-1):
        p1 = forma2D[i]
        p2 = forma2D[i+1]
        #para fazer uma linha
        vertices.append(batch.add(2, pyglet.gl.GL_LINES, None, ('v2i', (p1[0], p1[1], p2[0], p2[1]))))

    #para conectar a ultima reta
    p1 = forma2D[len(forma2D)-1]
    p2 = forma2D[0]
    vertices.append(batch.add(2, pyglet.gl.GL_LINES, None, ('v2i', (p1[0], p1[1], p2[0], p2[1]))))

#desenha o poligono inicial
draw_poligon(forma)

#cria a janela do pyglet
window = pyglet.window.Window()

#trata os eventos de pressionamento das teclas
@window.event
def on_key_press(symbol, modifiers):
    global forma
    if symbol == pyglet.window.key.RIGHT:
        print("->")
        forma_t = []
        for p in forma:
            forma_t.append((p[0]+10,p[1]))
        forma = forma_t
    elif symbol == pyglet.window.key.LEFT:
        print("<-")
        forma_t = []
        for p in forma:
            forma_t.append((p[0]-10, p[1]))
        forma = forma_t
    elif symbol == pyglet.window.key.UP:
        print("^")
        forma_t = []
        for p in forma:
            forma_t.append((p[0], p[1]+10))
        forma = forma_t
    elif symbol == pyglet.window.key.DOWN:
        print("v")
        forma_t = []
        for p in forma:
            forma_t.append((p[0], p[1]-10))
        forma = forma_t
    elif symbol == pyglet.window.key.PLUS:
        print("+")
        x=0
        y=0
        for p in forma:
            x += p[0]
            y += p[1]
        xref = x / len(forma)
        yref = y / len(forma)

        forma_t = []
        for p in forma:
            x = p[0] - xref
            y = p[1] - yref

            x *= 1.5
            y *= 1.5

            x += xref
            y += xref

            forma_t.append((int(x), int(y)))
        forma = forma_t
    elif symbol == pyglet.window.key.R:
        print("R")
        x=0
        y=0
        for p in forma:
            x += p[0]
            y += p[1]
        xref = x / len(forma)
        yref = y / len(forma)

        forma_t = []
        rad = 10 * math.pi/180

        for p in forma:
            x = p[0] - xref
            y = p[1] - yref

            xr = x * math.cos(rad) - y * math.sin(rad)
            yr = x * math.sin(rad) + y * math.cos(rad)

            xr += xref
            yr += xref

            forma_t.append((int(xr), int(yr)))

        forma = forma_t
    elif symbol == pyglet.window.key.E:
        print("E")
        x = 0
        y = 0
        for p in forma:
            x += p[0]
            y += p[1]
        xref = x / len(forma)
        yref = y / len(forma)

        forma_t = []

        for p in forma:
            x = p[0] - xref
            y = p[1] - yref

            x *= -1
            y *= -1

            x += xref
            y += yref

            forma_t.append((int(x), int(y)))
        forma = forma_t

    draw_poligon(forma)

#Desenha a tela
@window.event
def on_draw():
    window.clear()
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    batch.draw()
    print(forma)

pyglet.app.run()


