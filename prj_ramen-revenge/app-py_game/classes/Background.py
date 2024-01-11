from pyglet import image
from pyglet import sprite


class Background:
  def __init__(self, SCREEN_SIZE, scale:float):
    self.SCREEN_SIZE = SCREEN_SIZE
    self.img = image.load('./assets/images/background.png')
    self.sprite = sprite.Sprite(self.img)
    self.scale = scale
    self.sprite.scale = self.scale

  def draw(self):
    for i in range(0, self.SCREEN_SIZE[0], int(self.img.width * self.scale)):
      for j in range(0, self.SCREEN_SIZE[1], int(self.img.height * self.scale)):
        self.sprite.position = (i-1,j-1,0)
        self.sprite.draw()