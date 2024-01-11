import pyglet, cv2
import settings


IMAGES = settings.get_images()

def get_label_style(w,h):
  return {'font_name':'Times New Roman', 'font_size':36, 'x':w/2, 'y':h/2, 'anchor_x':'center', 'anchor_y':'center'}


def create_game_window(image, pos=(50,50)):

  pyglet_image = pyglet.image.load(image)
  h, w = cv2.imread(image).shape[0:2]

  pyglet_window = pyglet.window.Window(w, h, "pyglet_windows_test_1") #, style=pyglet_window.Window.WINDOW_STYLE_DIALOG) # , resizable=True)
  pyglet_window.set_icon(pyglet.image.load(settings.get_favicon()))
  pyglet_window.set_location(pos[0], pos[1])
  pyglet_label = pyglet.text.Label('Window 1', **get_label_style(pyglet_window.width, pyglet_window.height))
  pyglet_sprite = pyglet.sprite.Sprite(pyglet_image, x=0, y=0)

  @pyglet_window.event
  def on_draw():
    pyglet_window.clear()
    pyglet_label.draw()
    pyglet_sprite.draw()

create_game_window(IMAGES[0])
create_game_window(IMAGES[1])
create_game_window(IMAGES[2])
create_game_window(IMAGES[3])
create_game_window(IMAGES[4])
create_game_window(IMAGES[5])
create_game_window(IMAGES[6])
create_game_window(IMAGES[7])

pyglet.app.run()
