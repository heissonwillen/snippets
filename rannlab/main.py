import requests
import json

URL = "http://smartgsc.rannlabprojects.com/api/CMS/SearchAdvertisement"
body = {
    "Gender": "All",
    "MacAddress": "b8:27:eb:45:c7:21",
    "Location": "",
    "Business": "",
    "Age": ""
}

response = requests.post(URL, data=body)
videos = json.loads(response.json())

videos_urls = [video["VideoUrl"] for video in videos]

print(videos_urls)
