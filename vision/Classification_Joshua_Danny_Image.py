# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:58:48 2020

@author: blessonj

Code to train the Custom Vision Cognitive Service

Using the pip install azure-cognitiveservices-vision-customvision==2.0.0

The current version is 3.0.0
"""

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials

ENDPOINT = "https://packimagerecogniti-prediction.cognitiveservices.azure.com/"

# Replace with a valid key
training_key = "1d09912649e14a70a777687237b4e39d"
prediction_key = "8a6e3ffc93d84b6ab547d944612e8b9c"
prediction_resource_id = "/subscriptions/ba66f898-5c3d-473b-953e-fefd816b4264/resourceGroups/packing/providers/Microsoft.CognitiveServices/accounts/packimagerecogniti-Prediction"

publish_iteration_name = "classifyMyChildren"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
print ("Creating project...")
project = trainer.create_project("ClassifyMyChildren")

# Make two tags in the new project


Danny_tag  = trainer.create_tag(project.id, "Danny")
Joshua_tag = trainer.create_tag(project.id, "Joshua")


base_image_url = "C:\\Users\\blessonj\\Python\\"

print("Adding images...")

image_list = []
batching_list = []

for image_num in range(1,12):
    file_name = "Danny_{}.jpg".format(image_num)
    with open(base_image_url + "Danny\\" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[Danny_tag.id]))
        

for image_num in range(1, 8):
    file_name = "Joshua_{}.jpg".format(image_num)
    with open(base_image_url + "Joshua\\" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[Joshua_tag.id]))
        '''batching_list.append=ImageFileCreateBatch(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[hemlock_tag.id]), tag_ids=[hemlock_tag.id])'''

upload_result = trainer.create_images_from_files(project.id,images=image_list)
if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)
    
    
import time

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Publish it to the project endpoint
trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
print ("Done!")
        