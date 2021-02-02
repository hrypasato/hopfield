"""
Example of use Hopfield Recurrent network
=========================================

Task: Recognition of Simpsons

"""
import cv2, glob
import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

IMAGE_SIZE = (48, 48, 3) #size 48x48 pixels
TEST_PATH = './data/test/*.png'
TRAIN_PATH = './data/train/*.png'

def img2array(name):
  img = cv2.imread(name) #read binary image
  img = img.flatten() #Return a copy of the array collapsed into one dimension.
  img[img == 255] = 1
  return img

def array2img(array):
  array[array == -1] = 0
  array *= 255 # assing white spaces
  img = np.reshape(array,IMAGE_SIZE) #transform one dimension array to multidimension array
  return img

def array2float(array):
  tmp = np.asfarray(array)
  tmp[tmp == 0] = -1 
  return tmp

def show_images(images):
  fig = plt.figure()

  ax = fig.add_subplot(1, 2, 1)
  imgplot = plt.imshow(images[0])
  ax.set_title('Test')

  ax = fig.add_subplot(1, 2, 2)
  imgplot = plt.imshow(images[1])
  ax.set_title('Result')

  plt.show()



target = []
for file in glob.glob(TRAIN_PATH):
  array = img2array(file)
  target.append(array)

target = array2float(target)

net = nl.net.newhop(target) # Create and train network


img_test = img2array('./data/test/lisa1.png')
test = array2float(img_test)

out = net.sim([test]) #test network

out_image = array2img(out[0]) #output network image
img_test = array2img(test) #test image
show_images([img_test, out_image])