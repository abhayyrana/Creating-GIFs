import imageio
import cv2
import imageio.v3 as iio

filenames = ['chicklet_gif/chicklet1.png',
             'chicklet_gif/chicklet2.png',
             'chicklet_gif/chicklet3.png',
             'chicklet_gif/chicklet4.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('chicklet.gif', images, duration = 200, loop = 0)