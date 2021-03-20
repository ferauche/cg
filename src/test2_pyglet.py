import pyglet

window = pyglet.window.Window()

#coordenadas iniciais da reta
x = 0
y = 0

def update(dt):
    global x,y
    x += 1
    y += 1

pyglet.clock.schedule_interval(update,1/90) #chama update a cada 90 vezes por segundo

@window.event
def on_draw():
    pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,('v2i',(x,y)))

pyglet.app.run()
