import imageio
import cv2
import imageio.v3 as iio

filenames = ['dino_gif/dino1.png',
             'dino_gif/dino2.png',
             'dino_gif/dino3.png',
             'dino_gif/dino4.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('dino.gif', images, duration = 200, loop = 0)