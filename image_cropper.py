import cv2
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

#output_path = 
#dimension of screenshot 2160 x 1080
directory = "/usr/local/google/home/brywong/lux_cct (copy)/0.05"

new_dir = "0.05_resized"
path = os.path.join("/usr/local/google/home/brywong/lux_cct (copy)", new_dir)
#os.makedirs(path)
#print("Directory '% s' created" % directory) 



#prints image dimensions
#print(img.shape)

#print(imgResize.shape)

#name of file
for file_name in os.listdir(directory):
    print("Processing %s" % file_name)
    
    #img = cv2.imread(directory)
    img = cv2.imread(os.path.join(directory, file_name))
    imgCropped = img[300:1600,0:1080]
    #size of new image
    width, height = 1000, 1000
    imgResize = cv2.resize(imgCropped,(width,height))
    
    image = Image.open(os.path.join(directory, file_name))

      
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    image = Image.fromarray(imgResize)
    draw = ImageDraw.Draw(image)
    draw.text((150, 500), file_name, font=font, fill='rgb(255, 0, 0)')
     
    
    name = "edited_" + file_name
    file_path = os.path.join(path, name)
    image.save(file_path)
    #cv2.imwrite(os.path.join(file_path, name, img))

#cv2.imshow("test",img)
#cv2.imshow("Test",img)
#cv2.imshow("Test Cropped",imgCropped)

#cv2.imshow("Test Resized",imgResize)
#filename = 'savedImage.jpg'

print(file_path)

cv2.waitKey(0)