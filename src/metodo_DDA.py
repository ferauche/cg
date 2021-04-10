import pyglet

#coordenadas iniciais da reta
p1 = [int(i) for i in input("Entre com as coordenadas de P1 x y: ").split()]
p2 = [int(i) for i in input("Entre com as coordenadas de P2 x y: ").split()]

dx = p2[0] - p1[0]
dy = p2[1] - p1[1]

reta = []

if dx == 0:
    for y in range(p1[1], p2[1]):
        reta.append(p1[0])
        reta.append(y)
elif dy == 0:
    for x in range(p1[0], p2[0]):
        reta.append(x)
        reta.append(p1[1])
elif dx > dy:
    inc = dy / dx
    y = p1[1]
    for x in range(p1[0], p2[0]):
        reta.append(x)
        reta.append(round(y))
        y = y+inc
else:
    inc = dx / dy
    x = p1[0]
    for y in range(p1[1], p2[1]):
        reta.append(round(x))
        reta.append(y)
        x = x+inc

print(reta)
window = pyglet.window.Window()

@window.event
def on_draw():
    global reta
    pyglet.graphics.draw(int(len(reta)/2),pyglet.gl.GL_POINTS,('v2i', reta))


pyglet.app.run()