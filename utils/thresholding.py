'''
Objetive: remove the background and focus the object

Threshold types
0 - Binary
1 - Binary Inverted
2 - Truncated
3 - Threshold to zero
4 - Threshold to zero inverted
'''
import cv2, glob

BINARY = 0
THRESHOLD_VALUE = 141
TEST_PATH = '../data/test/*.png'
TRAIN_PATH = '../data/train/*.png'

def new_name(name):
    return name.replace('g.png','.png')

def threshold_image(path):
    for file in glob.glob(path):
        image = cv2.imread(file)
        #apply threshold
        _, img1 = cv2.threshold(image,THRESHOLD_VALUE, 255, BINARY)
        cv2.imwrite(new_name(file), img1) #save image

threshold_image(TEST_PATH)
threshold_image(TRAIN_PATH)