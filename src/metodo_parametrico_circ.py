import pyglet
import math

#coordenadas iniciais da reta
p1 = [int(i) for i in input("Entre com as coordenadas do centro da circunferencia: ").split()]
p2 = [int(i) for i in input("Entre com as coordenadas de um ponto da circunferência: ").split()]

raio = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))

delta_pi = math.pi / 360

circ = []
t = 0

while (t <= (2*math.pi) ):
    x = p1[0]+round(raio*math.cos(t))
    y = p1[1]+round(raio*math.sin(t))
    circ.append(x)
    circ.append(y)

    t += delta_pi

print(circ)
print(len(circ)/2)
window = pyglet.window.Window()

@window.event
def on_draw():
    global circ
    pyglet.graphics.draw(int(len(circ)/2),pyglet.gl.GL_POINTS,('v2i', circ))


pyglet.app.run()