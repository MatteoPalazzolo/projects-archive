from __future__ import annotations
import json
from typing import List
from classes.Collision import Collision
import glob, random, os
from pyglet import image
from pyglet.sprite import Sprite
from pyglet.graphics import Batch, Group



## IMPORT JSON
with open('./settings.json') as json_file:
  SETTINGS = json.load(json_file)



class Food:

  def __init__(self, foods:List[Food], batch:Batch, collision_batch:Batch, x=0, y=0):
    self.foods = foods
    self.food = random.choice(SETTINGS['FOOD']['TYPES'])
    self.speed = self.food['SPEED']
    self.scale = self.food['SCALE']
    self.img = image.load(SETTINGS['FOOD']['SPRITE_DIR'].format(self.food['NAME']))
    self.img.anchor_x = self.img.width // 2
    self.img.anchor_y = self.img.height // 2
    self.sprite = Sprite(img=self.img, x=x, y=y, batch=batch)
    self.sprite.scale = self.scale
    self.collision = Collision(range=self.img.height * self.scale // 2, position=self.sprite.position, batch=collision_batch)

  def set_position(self, x, y):
    self.sprite.x = x
    self.sprite.y = y
    self.collision.set_position([x, y])

  def move(self, x, y):
    self.sprite.x += x
    self.sprite.y += y
    self.collision.move(x, y)

  def destroy(self):
    self.foods.remove(self)
