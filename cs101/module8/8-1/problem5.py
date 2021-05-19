from cs1media import *
import math

### example ###
def chroma(img, key, threshold):
  w, h = img.size()
  for y in range(h):
    for x in range(w):
      p = img.get(x, y)
      if dist(p, key) < threshold:
        img.set(x, y, Color.yellow)

### problem ###
def image_inversion(img):
  w, h = img.size()
  img_inv = create_picture(w, h)

  # put your code
  for y in range(h):
    for x in range(w):
      p = img.get(x, y)
      # print(type(p), p)
      img_inv.set(x, y, (255-p[0], 255-p[1], 255-p[2]))

  return img_inv

img = load_picture("photos/statue1.jpg")
# chroma(statue, (41, 75, 146), 70)

# img.show()
img_inv = image_inversion(img)
img_inv.show()
img_inv.save_as("photos/statue1_inv.jpg")
