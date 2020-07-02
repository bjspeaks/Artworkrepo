# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:26:19 2020

@author: blessonj
Convert pdf to image file
The pypi library link: https://pypi.org/project/pdf2image/
"""
import glob
import tempfile

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)




base_pdf_url = "C:\\Users\\blessonj\\Python\\pdfs\\"
output_path = "C:\\Users\\blessonj\\Python\\jpeg_files\\"
pdf_num = 1

pdf_files = []
for file in glob.glob(base_pdf_url+"*.pdf"):
    pdf_files.append(file)
    

print("Initialised the pdf url variable...")



'''
for pdf_num in range(1,12):
    file_name = "PDF_{}.pdf".format(pdf_num)
    full_path = base_pdf_url+file_name
    print(full_path)
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(full_path, output_folder=output_path)
    # Do something here
   
'''

for pdf_file in pdf_files:
    ##file_name = "PDF_{}.pdf".format(pdf_num)
    ##full_path = base_pdf_url+file_name
    print(pdf_file)
    images = convert_from_bytes(open(pdf_file,'rb').read())
    for i,image in enumerate(images):
        fname = "image_" + str(pdf_num)+"_"+str(i) + ".jpg"
        image_folder= output_path+fname
        image.save(image_folder, "jpeg")
    pdf_num +=1 

 