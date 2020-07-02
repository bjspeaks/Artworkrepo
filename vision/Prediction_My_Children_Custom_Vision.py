# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:57:57 2020

@author: blessonj
"""

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.operations import CustomVisionTrainingClientOperationsMixin
from msrest.authentication import ApiKeyCredentials

# Replace with a valid key
training_key = "1d09912649e14a70a777687237b4e39d"
prediction_key = "8a6e3ffc93d84b6ab547d944612e8b9c"
prediction_resource_id = "/subscriptions/ba66f898-5c3d-473b-953e-fefd816b4264/resourceGroups/packing/providers/Microsoft.CognitiveServices/accounts/packimagerecogniti-Prediction"

## Set the project Name

project_name = "ClassifyMyChildren"
publish_iteration_name = "classifyMyChildren"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
ENDPOINT = "https://packimagerecogniti-prediction.cognitiveservices.azure.com/"

trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

base_image_url = "C:\\Users\\blessonj\\Python\\cognitive-services-python-sdk-samples\\samples\\vision\\"

## Get the project id from the list of projects
## Isolate the one that is doing classification

projects = []
projects = trainer.get_projects()

for project in projects:
    
    if project.name == project_name:
        #print(project.id)
        project_id = project.id
        print(project_id)



with open(base_image_url + "images\\Test\\Test_Joshua.jpg", "rb") as image_contents:
    results = predictor.classify_image(
        projects[0].id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
