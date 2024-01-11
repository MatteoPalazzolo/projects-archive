import pyglet, math, numpy
from pyglet import shapes
from pyglet.window import key
import COLORS as colors


### CONSTS ###

WIDTH, HEIGHT = 1920//2, 1080//2



### CODE ###

game_window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
batch = pyglet.graphics.Batch()

keyboard = key.KeyStateHandler()
game_window.push_handlers(keyboard)

arc = shapes.Arc(110, 110, 100, segments=10, angle=math.radians(270), start_angle=0, closed=True, color=colors.RED1, batch=batch)


@game_window.event
def on_draw():
    game_window.clear()
    batch.draw()
    
"""
@game_window.event
def on_key_press(symbol, modifiers):
  if symbol == pyglet.window.key.W:
      circle.y += 30
  elif symbol == pyglet.window.key.S:
      circle.y -= 30
  elif symbol == pyglet.window.key.A:
      circle.x -= 30
  elif symbol == pyglet.window.key.D:
      circle.x += 30
"""
"""
@game_window.event
def on_key_press(symbol, modifiers):
  if symbol == key.W:
    arc.angle += math.radians(10)
  elif symbol == key.S:
    arc.angle -= math.radians(10)
  elif symbol == pyglet.window.key.A:
    arc.opacity -= 10
  elif symbol == pyglet.window.key.D:
    arc.opacity += 10
  arc.opacity = numpy.clip(arc.opacity, 0, 255)
"""

def update(dt):
  if keyboard[key.D]:
    arc.angle += math.radians(10)
  elif keyboard[key.A]:
    arc.angle -= math.radians(10)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()