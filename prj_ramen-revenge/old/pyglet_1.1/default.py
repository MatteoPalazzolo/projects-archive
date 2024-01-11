import pyglet


### CONSTS ###

WIDTH, HEIGHT = 1920//2, 1080//2



### CODE ###

game_window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

@game_window.event
def on_draw():
    game_window.clear()
    pass





def update(dt):
  pass

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()