import pyglet, math, numpy, time
from pyglet import shapes
from pyglet.window import key
import COLORS as colors


### CONSTS ###

WIDTH, HEIGHT = 1920//2, 1080//2



### DEF ###

def sin_func(offset, x1, x2, q, step=10):
  points = []
  for x in range(0,x2-x1+step,step):
    y = math.sin(math.radians(x+x1)) * 50
    points.append((x+x1, y+q))
    print((x+x1, y+q))
  return points



### CODE ###

win = pyglet.window.Window(width=WIDTH, height=HEIGHT)
batch = pyglet.graphics.Batch()


# https://pyglet.readthedocs.io/en/latest/modules/shapes.html

arc = shapes.Arc(110, 110, 100, segments=10, angle=math.radians(270), start_angle=0, closed=True, color=colors.RED1, batch=batch)
arc.opacity = numpy.clip(arc.opacity, 0, 255)

line = shapes.Line(200, 0, 300, 300, width=10, color=colors.CYAN4, batch=batch)

# polygon = shapes.Polygon(*sin_func(0, WIDTH, 100, 10), color=colors.TEAL, batch=batch)
# polygon = shapes.Polygon(*sin_func(0, WIDTH, 300, 10), (WIDTH, 0), (0, 0), color=colors.TEAL, batch=batch)


fps_display = pyglet.window.FPSDisplay(window=win)

@win.event
def on_draw():
    win.clear()
    batch.draw()
    fps_display.draw()

lines = []
points = sin_func(time.time(), 10, WIDTH, 300, 25)
for i, p in enumerate(points):
  try:
    lines.append(shapes.Line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], width=2, color=colors.CYAN4, batch=batch))
  except IndexError:
    pass

def update(dt):
  pass

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()