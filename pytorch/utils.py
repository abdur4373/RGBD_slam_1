
from PIL import Image

from skimage import img_as_float

def center_crop(image, cropX, cropY):
    y, x, d = image.shape

    startX = x - cropX

    startY = y - cropY

    return image[(startY//2):y-(startY//2), (startX//2):x-(startX//2), :]


def down_size(image,size_x,size_y):

    Img = image.resize((size_x,size_y), Image.ANTIALIAS)

    Img = img_as_float(Img)


    return Img


