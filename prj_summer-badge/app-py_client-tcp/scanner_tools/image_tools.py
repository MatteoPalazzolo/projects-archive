################# IMPORT #################
from PIL import Image
from io import BytesIO

################# DEF #################
def image_to_bytes(image:Image) -> bytes:
    bytes_io = BytesIO()
    image.save(bytes_io, format="png")
    return bytes_io.getvalue()

def manage_image(image:Image) -> Image:
    SCALE = .9

    # CROP
    w, h = image.size
    left, top, right, bottom = w/2 - h/2, 0, w/2 + h/2, h
    image = image.crop((left, top, right, bottom))

    # RESIZE
    while True:
        if get_image_size(image) > 64000: # mysql BLOB size
            image = scale_image(image, SCALE)
        else:
            break

    return image

def scale_image(image:Image, fact:float) -> Image:
    w, h = image.size
    size = int(w * fact), int(h * fact)
    image = image.resize(size, Image.ANTIALIAS) # Image.NEAREST
    return image

def get_image_size(img:Image) -> int:
    img_file = BytesIO()
    img.save(img_file, 'png')
    img_size = img_file.tell()
    return img_size

################# CODE #################
if __name__ ==  "__main__":
    pass