import random, cv2, math
import settings


# check if point is inside a rectangle
def point_in_rect(point=(0,0), rect=("x","y","w","h")) -> bool:
  in_x = rect[0] <= point[0] <= rect[0] + rect[2]
  in_y = rect[1] <= point[1] <= rect[1] + rect[3]
  return in_x and in_y

# check if two rectangles are overlapping (works perfectly only with rectangle of the same size)
def rect_in_rect(rect1=("x","y","w","h"), rect2=("x","y","w","h")) -> bool:
  point00 = [rect1[0], rect1[1]]
  point11 = [rect1[0] + rect1[2], rect1[1] + rect1[3]]
  point10 = [rect1[0] + rect1[2], rect1[1]]
  point01 = [rect1[0], rect1[1] + rect1[3]]
  return point_in_rect(point00, rect2) or point_in_rect(point11, rect2) or point_in_rect(point10, rect2) or point_in_rect(point01, rect2)

# get magnitude of the vector [w,h] of an image
def get_image_magnitude(img) -> float:
  size = cv2.imread(img).shape[0:2]
  magnitude = math.sqrt(sum(pow(element, 2) for element in size))
  return magnitude

# generate random position on screen
def get_random_position(w, h):
  x = random.randint(0, settings.SCREEN_WIDTH - w - settings.MARGIN_X)
  y = random.randint(0, settings.SCREEN_HEIGHT - h - settings.MARGIN_Y)
  return (x, y)


def get_pseudorandom_position(w, h, WINDOWS_RECT):

  # try to generate multiple random values and to validate them
  for i in range(10):

    # get random coordinates
    x, y = get_random_position(w, h)

    # if WINDOWS_TRANSFORM is empty -> return the random values
    if len(WINDOWS_RECT) == 0:
      WINDOWS_RECT.append((x, y, w, h))
      return (x, y)

    # count how many windows are not overlapping the coordinates
    collided = False
    for window_rect in WINDOWS_RECT:
      #if tools.is_point_in_rectangle([x, y], window_rect):
      if rect_in_rect((x, y, w, h), window_rect):
        collided = True
    
    # if no window is overlapping the coordinates -> return the coordinates
    if not collided:
      #print("i", i)
      WINDOWS_RECT.append((x, y, w, h))
      return (x, y)

  # if after the for loop end return random values in order to avoid infinite loops
  #print("failed")
  WINDOWS_RECT.append((x, y, w, h))
  return (x, y)

