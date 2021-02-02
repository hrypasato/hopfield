#convert images to gray and scale to 48x48 pixels
from skimage import io, color, data
import glob, cv2

def new_name(name):
    return name.replace('.png','g.png')
    
for file in glob.glob('../data/*.png'):
    img = cv2.imread(file)
    dsize = (48,48) #new size
    
    gray_img = color.rgb2gray(img) #conver to grayscale
    gray_img = cv2.resize(gray_img,dsize, interpolation = cv2.INTER_AREA)
    gray_img *= 255
    cv2.imwrite(new_name(file),gray_img)#save image