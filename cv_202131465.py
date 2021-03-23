# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 08:20:42 2021

https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html

@author: DeskTop
"""

"""
homework: resize all imgs in the directory with new (w, h)
make a function with default arguments (w = 300, h = 300)
save each file with suffix (fn_resized.jpg)
make a function to check all new images in the directory 
(with timedelay = default argument:2000)
hint: import glob # imgs = glob.glob("*.jpg")

"""

# <<=== ACTUAL CODE STARTS HERE ===>>


# import required libraries
import cv2
import glob

# function that resizes image
def resize_image(image, w = 300, h = 300):
    img_color = cv2.imread(image, 1) # read image as RGB mode
    img_cnew = cv2.resize(img_color, (w, h)) # resize image
    # make up a new name
    # take of '.jpg' of the original file name (string slicing used)
    # attach "_resized.jpg" instead at the end.
    fname_new = image[:-4] + "_resized.jpg"
    # write the file to the directory
    cv2.imwrite(fname_new, img_cnew)

# function that display cropped images
def display_new_image():
    # add files ending in "_resized.jpg" to a new list
    new_imgs = glob.glob("*_resized.jpg")
    for new_image in new_imgs:
        # read as image type
        new_image_color = cv2.imread(new_image, 1)
        # display image in a window
        cv2.imshow('Check Images', new_image_color)
        # delay of 2000ms (2 seconds)
        cv2.waitKey(2000)
    # after displaying all images, destroy the window.
    cv2.destroyAllWindows()

# MAIN FUNCTION
def main():
    # retrive all JPG files in the directory
    imgs = glob.glob("*.jpg")
    # resize images
    for image in imgs:
        resize_image(image)
    # display cropped images
    display_new_image()

# execute MAIN function
main()