import requests, os

# script to scrape the data for all images from 
# https://www.effectgames.com/demos/canvascycle

# grabbed from the html of the page
ids = [
    "V08AM",
    "V29",
    "V19",
    "V26SNOW",
    "V08RAIN",
    "V14",
    "V30",
    "V04",
    "V07",
    "V20",
    "V05RAIN",
    "V08PM",
    "V16RAIN",
    "V19AURA",
    "CORAL",
    "V15",
    "V30RAIN",
    "V02",
    "V28",
    "V29PM",
    "V16",
    "V01",
    "V09",
    "V16PM",
    "V08",
    "V03",
    "V05HAUNT",
    "V10",
    "V11AM",
    "V13",
    "V17",
    "V19PM",
    "V25HEAT",
    "V27",
    "V29FOG",
]

base_url = "https://www.effectgames.com/demos/canvascycle"

def create_dir(path:str):
    if not os.path.exists(path):
        os.mkdir(path)

create_dir("scraped/")
create_dir("scraped/images")
create_dir("scraped/audio")

image_count = 0
audio_count = 0

def fetch_id(id:str):
    global image_count, audio_count
    image_path = f"scraped/images/{id}.LBM.json"
    audio_path = f"scraped/audio/{id}.ogg"
    fetch_image = not os.path.exists(image_path)
    fetch_audio = not os.path.exists(audio_path)

    if fetch_image:
        filename = id+".LBM.json"
        url = base_url+"/images/"+filename
        response = requests.get(url)
        with open(image_path,"wb") as f:
            f.write(response.content)
        print(f"{id}: fetched image !")
        image_count += 1
    if fetch_audio:
        filename = id+".ogg"
        url = base_url+"/audio/"+filename
        response = requests.get(url)
        with open(audio_path,"wb") as f:
            f.write(response.content)
        print(f"{id}: fetched audio !")
        audio_count += 1

for id in ids:
    fetch_id(id)

print(f"all done! fetched {image_count} images and {audio_count} audio files")