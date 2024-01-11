from classes.Collision import Collision
import numpy
from pyglet import image
from pyglet.sprite import Sprite


class Player:
  def __init__(self, SCREEN_SIZE, collision_batch):
    SCALE = .1
    self.SCREEN_SIZE = SCREEN_SIZE
    self.speed = 10
    self.img = image.load('./assets/images/bowl.png')
    self.img.anchor_x = self.img.width // 2
    self.img.anchor_y = self.img.height // 2
    self.size = [self.img.width * SCALE, self.img.height * SCALE]
    self.sprite = Sprite(img=self.img, x=int(SCREEN_SIZE[0]*.5), y=int(SCREEN_SIZE[1]*.13))
    self.sprite.scale = SCALE
    self.collision = Collision(range=self.img.height * SCALE // 2, position=self.sprite.position, batch=collision_batch)

  def move(self, dx):
    x = self.sprite.x + dx
    start = self.size[0] // 2
    end = self.SCREEN_SIZE[0] - self.size[1] // 2
    nx = numpy.clip(x, start, end)
    self.sprite.x = nx
    self.collision.set_position([nx, self.sprite.y, 0])

  def draw(self):
    self.sprite.draw()


  
