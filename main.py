"""Detect text in a video stored on GCS."""
from google.cloud import videointelligence
import json

#filename = 'result.json'

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.TEXT_DETECTION]

#gcs_uri = "" Path do arquivo virá por evento no storage

operation = video_client.annotate_video(
    request={"features": features, "input_uri": gcs_uri}
)

print("\nProcessing video for text detection.")
result = operation.result(timeout=600)


annotation_result = result.annotation_results[0]

data=[]
for text_annotation in annotation_result.text_annotations:
    if text_annotation.text[0] == "+":
        item = {"number": text_annotation.text}
        data.append(item)

#Caso queiram usar o salvamento do arquivo é só usar o código abaixo
#Se não só trocar pela chama de API

#with open(filename, 'w') as json_file:
#    json.dump(data, json_file, 
#                       indent=4,  
#                       separators=(',',': '))
 
#print('Successfully appended to the JSON file')   
