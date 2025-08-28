import imageio
import cv2
import imageio.v3 as iio

filenames = ['hippocorn_gif/hippocorn1.png',
             'hippocorn_gif/hippocorn2.png',
             'hippocorn_gif/hippocorn3.png',
             'hippocorn_gif/hippocorn4.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('hippocorn.gif', images, duration = 200, loop = 0)