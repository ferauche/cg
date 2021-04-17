import pyglet
import math

#coordenadas iniciais da reta
p1 = [int(i) for i in input("Entre com as coordenadas do centro da circunferencia: ").split()]
p2 = [int(i) for i in input("Entre com as coordenadas de um ponto da circunferência: ").split()]

raio = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))

circ = []
count = 0

x = 0
y = round(raio)

while y >= 0:
    circ.append(p1[0] + x)
    circ.append(p1[1] + y)
    circ.append(p1[0] + x)
    circ.append(p1[1] - y)
    circ.append(p1[0] - x)
    circ.append(p1[1] + y)
    circ.append(p1[0] - x)
    circ.append(p1[1] - y)

    circ.append(p1[1] + y)
    circ.append(p1[0] + x)
    circ.append(p1[1] + y)
    circ.append(p1[0] - x)
    circ.append(p1[1] - y)
    circ.append(p1[0] + x)
    circ.append(p1[1] - y)
    circ.append(p1[0] - x)

    delta_i = (x+1)**2 + (y-1)**2 - raio ** 2
    md = abs(delta_i)

    if delta_i < 0:
        mh = abs((x+1)**2 + (y-1)**2 - raio**2)
        sigma = mh - md
        if sigma <= 0:
            x += 1
        else:
            x += 1
            y -= 1
    elif delta_i > 0:
        mv = abs((x**2) + (y-1)**2 - raio**2)
        sigma = mv - md
        if sigma >= 0:
            x += 1
            y -= 1
        else:
            y -= 1
    else:
        x += 1
        y -= 1

    count += 1

print(circ)
print(len(circ)/2)
print(count)

window = pyglet.window.Window()

@window.event
def on_draw():
    global circ
    pyglet.graphics.draw(int(len(circ)/2),pyglet.gl.GL_POINTS,('v2i', circ))


pyglet.app.run()