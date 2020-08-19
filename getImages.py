import sys
import os
import json
import requests
import shutil

FOLDER = sys.argv[0]
FOLDER = os.path.abspath(FOLDER + "/..") + "/"

FILE = "face_detection.json"

with open(FOLDER + FILE) as f:
    Lines = f.readlines() 

print("Descargando imagenes...")
for line in Lines: 
    data = json.loads(line)
    image_url = data['content']
    NAME_IMAGE = image_url.split("/")[-1]
    filename = FOLDER + "/" + "images/" + NAME_IMAGE
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        
        print('Image sucessfully Downloaded: ',NAME_IMAGE)

print("Todas las imagenes descargadas")