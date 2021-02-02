#extract data from image and save into excel
#Getting Pixel Values
from skimage import io
import pandas as pd
import glob

TEST_PATH = '../data/test/*.png'
TRAIN_PATH = '../data/train/*.png'
TEST_NAME = 'test.xlsx'
TRAIN_NAME = 'train.xlsx'

def get_data(path,name):
    df = pd.DataFrame()
    c = 0
    for file in glob.glob(path):
        img = io.imread(file)
        df.insert(c,str(c),img.flatten())
        c += 1
    
    df.to_excel(name, index=False)

get_data(TEST_PATH,TEST_NAME)
get_data(TRAIN_PATH,TRAIN_NAME)