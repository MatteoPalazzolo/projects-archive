from __future__ import annotations
import math
from pyglet import shapes

DEBUG_COLOR = (50, 225, 30, 150)


class Collision:
  
  def __init__(self, range, position, batch):
    self.range = range
    self.position = list(position)
    self.circle = shapes.Circle(radius=self.range, x=self.position[0], y=self.position[1], color=DEBUG_COLOR, batch=batch)

  def is_colliding(self, collision:Collision) -> bool:
    return math.dist(self.position, collision.position) < self.range + collision.range
  
  def set_position(self, position):
    self.position = list(position)
    self.circle.position = position[:2]

  def move(self, x, y):
    self.position[0] += x
    self.position[1] += y
    self.circle.x += x
    self.circle.y += y

