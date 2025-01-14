import cv2
import numpy as np


def convert_to_greyscale(image, image_path=None):
    if(image_path!=None):
        image=cv2.imread(image_path)
        
    image = np.array(image)
    
    grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return grey_image