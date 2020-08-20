# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:31:05 2020

@author: blessonj
"""

#### image manipulation libraries

from skimage import io,filters
from skimage.io import imread
from skimage.transform import resize,rescale,downscale_local_mean
from skimage.color import rgb2gray,grey2rgb
from matplotlib import pyplot as plt
import matplotlib.cm as cm

#### file browsing libraries

import glob
import tempfile

'''greyscale function'''
def rgb2greyscale(base_image_path,output_image_path):
    
    '''get all the image files'''
    image_files = []
    for file in glob.glob(base_image_path+"*.jpg"):
        image_files.append(file)
    
    image_count = 49
    
    print("Initialised the image url variables...")
    
    for image_file in image_files:
        ##file_name = "PDF_{}.pdf".format(pdf_num)
        ##full_path = base_pdf_url+file_name
        print(image_file)
        image_read = io.imread(image_file)
        image_filtered = rgb2gray(image_read)
        fname = "image"+"_"+str(image_count) + ".jpg"
        image_folder= output_image_path+fname
        image_filtered_rescaled = rescale(image_filtered,1.5,anti_aliasing=False)
        io.imsave(image_folder, image_filtered_rescaled)
        print(image_folder)
        ###image_filtered.save(image_folder, "jpeg")
        image_count+=1
        
'''stretch function'''
def stretchimage(base_image_path,output_image_path):
    
    '''get all the image files
       https://scikit-image.org/docs/dev/auto_examples/transform/plot_rescale.html
    '''
    image_files = []
    for file in glob.glob(base_image_path+"*.jpg"):
        image_files.append(file)
    
    image_count = 49
    
    print("Initialised the image url variables...")
    
    for image_file in image_files:
        ##file_name = "PDF_{}.pdf".format(pdf_num)
        ##full_path = base_pdf_url+file_name
        print(image_file)
        image_read = io.imread(image_file)
        image_stretched = rescale(image_read,1.12,anti_aliasing=False)
        fname = "image"+"_"+str(image_count) + ".jpg"
        image_folder= output_image_path+fname
        #image_stretched_color = grey2rgb(image_stretched)
        io.imsave(image_folder, image_stretched)
        print(image_folder)
        ###image_filtered.save(image_folder, "jpeg")
        image_count+=1



'''Initialize the path of the image file'''

## base_image_path = "C:\\Users\\blessonj\\Python\\jpeg_files_training\\NewTrainingSet\\"
base_image_path = "C:\\Users\\blessonj\\Python\\ArtWorkProject\\Collaterals\\jpeg_files_training\\"

'''Invoke the image manipulation functions'''

''' invoke greyscale function'''
output_image_path = "C:\\Users\\blessonj\\Python\\jpeg_files_training\\NewTrainingSet\\doctored_image\\rgb2gray\\"
rgb2greyscale(base_image_path,output_image_path)

'''stretch function'''
output_image_path = "C:\\Users\\blessonj\\Python\\jpeg_files_training\\NewTrainingSet\\doctored_image\\stretchimage\\"
stretchimage(base_image_path,output_image_path)

