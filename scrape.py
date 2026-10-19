import requests

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

fetch_image = True
fetch_audio = True

def fetch_id(id:str):
    if fetch_image:
        filename = id+".LBM.json"
        url = base_url+"/images/"+filename
        response = requests.get(url)
        with open(f"scraped/images/{filename}","wb") as f:
            f.write(response.content)
        print(f"{id}: fetched image !")
    if fetch_audio:
        filename = id+".ogg"
        url = base_url+"/audio/"+filename
        response = requests.get(url)
        with open(f"scraped/audio/{filename}","wb") as f:
            f.write(response.content)
        print(f"{id}: fetched audio !")

for id in ids:
    fetch_id(id)

print("all done!")