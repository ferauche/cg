import pyglet

#coordenadas iniciais da reta
p1 = [int(i) for i in input("Entre com as coordenadas de P1 x y: ").split()]
p2 = [int(i) for i in input("Entre com as coordenadas de P2 x y: ").split()]

dx = p2[0] - p1[0]
dy = p2[1] - p1[1]

x = p1[0]
y = p1[1]

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
    d = 2 * dy - dx
    for i in range(0,dx+1):
        reta.append(x)
        reta.append(y)
        if d >= 0:
            d = d + 2 * (dy - dx)
            y += 1
        else:
            d += 2 * dy
        x += 1
else:
    d = 2 * dx - dy
    for i in range(0, dy+1):
        reta.append(x)
        reta.append(y)
        if d >= 0:
            d = d + 2 * (dx - dy)
            x += 1
        else:
            d += 2 * dx
        y += 1

print(reta)
window = pyglet.window.Window()

@window.event
def on_draw():
    global reta
    pyglet.graphics.draw(int(len(reta)/2),pyglet.gl.GL_POINTS,('v2i', reta))


pyglet.app.run()