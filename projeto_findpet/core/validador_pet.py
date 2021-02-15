import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

def validarSeTemCachorroNaFoto(photo):
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GoogleVisionApiKey.json'

    client = vision_v1.ImageAnnotatorClient()

    content = photo.read()

    image = vision_v1.types.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    for object_ in objects:
        
        if object_.name == "Dog" and object_.score > 0.6 or object_.name == "Cat" and object_.score > 0.6:
            return True
        
    return False