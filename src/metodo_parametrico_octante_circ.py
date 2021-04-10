import pyglet
import math

#coordenadas iniciais da reta
p1 = [int(i) for i in input("Entre com as coordenadas do centro da circunferencia: ").split()]
p2 = [int(i) for i in input("Entre com as coordenadas de um ponto da circunferência: ").split()]

raio = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))

delta_pi = math.pi / 360

circ = []
t = 0
count = 0
while (t <= (math.pi/4) ):
    x = round(raio*math.cos(t))
    y = round(raio*math.sin(t))
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

    t += delta_pi
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