from PIL import Image
import os

STRENGHT = 12


# Open The Image to PIXELIZE
img = Image.open("image.jpg")

img.width
 
# The smallest is the resize, the biggest are the PIXELS
# imgSmall = img.resize((128, 128), resample=Image.BILINEAR)
# If you do want ANTIALISING uncomment the line above and comment the one below
imgSmall = img.resize((img.width // STRENGHT, img.height // STRENGHT))
 
# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size,Image.NEAREST)
 
# Save
result.save('result.png')
os.startfile('result.png')