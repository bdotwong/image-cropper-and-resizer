# Resize all images in a directory to half the size.
#
# Save on a new file with the same name but with "small_" prefix
# on high quality jpeg format.
#
# If the script is in /images/ and the files are in /images/2012-1-1-pics
# call with: python resize.py 2012-1-1-pics
from PIL import Image

#import Image
import os
import sys

directory = "/usr/local/google/home/brywong/lux_cct (copy)/0.05"

new_dir = "0.05_resized"
path = os.path.join("/usr/local/google/home/brywong/lux_cct (copy)", new_dir)
os.makedirs(path)
print("Directory '% s' created" % directory) 

for file_name in os.listdir(directory):
    print("Processing %s" % file_name)
    image = Image.open(os.path.join(directory, file_name))

    x,y = image.size
    new_dimensions = (x//2, y//2) #dimension set here
    output = image.resize(new_dimensions, Image.ANTIALIAS)


   


    output_file_name = os.path.join(path, "small_" + file_name)
    output.save(output_file_name, "PNG", quality = 95)

print("All done")