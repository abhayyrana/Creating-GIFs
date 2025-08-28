import imageio
import cv2
import imageio.v3 as iio

filenames = ['nyan_cat_gif/nyan-cat1.png',
             'nyan_cat_gif/nyan-cat2.png',
             'nyan_cat_gif/nyan-cat3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('nyan_cat.gif', images, duration = 200, loop = 0)