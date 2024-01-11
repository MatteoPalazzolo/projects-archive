import pyglet, random, colour, numpy, json
from pyglet import shapes, window, image, sprite, media, graphics
from pyglet.window import key
from classes.Food import Food
from classes.Player import Player
from classes.Background import Background
from my_shaders import useShaders



# # # # # #

score = 0
MADNESS = 0


## IMPORT JSON
with open('./settings.json') as json_file:
  SETTINGS = json.load(json_file)

## WINDOW
win = pyglet.window.Window(width=SETTINGS['SCREEN_SIZE'][0], height=SETTINGS['SCREEN_SIZE'][1])
shader = useShaders()

## SOUNDTRACK
pyglet.options['audio'] = ('openal', 'pulse', 'xaudio2', 'directsound', 'silent')
song = media.load('./assets/audio/song1.wav')
song.play()

## KEYBOARD
keyboard = key.KeyStateHandler()
win.push_handlers(keyboard)

## DISPLAY
bg = Background(SETTINGS['SCREEN_SIZE'], .4)
fps_display = window.FPSDisplay(win)
collision_batch = graphics.Batch()
food_batch = graphics.Batch()

## PLAYER
player = Player(SETTINGS['SCREEN_SIZE'], collision_batch)

## FOOD INSTANCES
foods = []

## UPDATE LOOP
def update(dt):

  # delta time adjustment
  dt = 1/60 or numpy.clip(dt, 0, 1/30)

  # player movement
  if keyboard[key.D]:
    player.move(1 * dt * SETTINGS['PLAYER']['SPEED'])
  elif keyboard[key.A]:
    player.move(-1 * dt * SETTINGS['PLAYER']['SPEED'])

  # food spawn
  global foods
  if random.randint(0, 50) < 1:
    foods.append(Food(
      foods = foods,
      x = random.random() * SETTINGS['SCREEN_SIZE'][0],
      y = SETTINGS['SCREEN_SIZE'][1] + 20,
      batch = food_batch,
      collision_batch = collision_batch
    ))


  for f in foods:
    # food fall
    f.move(0, -1 * SETTINGS['FOOD']['SPEED'] * f.speed * dt)

    # destroy food on collision with player
    if player.collision.is_colliding(f.collision):
      global score
      score += 1
      f.destroy()

    # destroy food if out of screen
    if f.sprite.y < -f.img.height:
      f.destroy()
    
  # print(len(foods))


@win.event
def on_draw():
  win.clear()

  # shader.use() shader.stop()
  # with shader as s:
  shader.use()
  # s.my_uniform = 1.0

  bg.draw()
  player.draw()
  food_batch.draw()

  if SETTINGS['COLLISION_DEBUG']:
    collision_batch.draw()
    fps_display.draw()
  
  shader.stop()



if __name__ == '__main__':
  pyglet.clock.schedule_interval(update, 1/60)
  pyglet.app.run()