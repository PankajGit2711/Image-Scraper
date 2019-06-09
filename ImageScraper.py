from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def InitiateSearch():

    search = input("Enter Your Search:   ")
    para = {"q" : search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    req = requests.get("http://www.bing.com/images/search", params = para)

    soup = BeautifulSoup(req.text, "html.parser")
    links = soup.findAll("a", {"class" : "thumb"})

    for item in links:
        try:
            obj_im = requests.get(item.attrs["href"])
            print("Getting: ", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                image = Image.open(BytesIO(obj_im.content))
                image.save('./' + dir_name + '/' + title, image.format)
            except:
                print("Oops!!! Could Not Save The Image You Requested.")
        except:
            print("Sorry!!! Could Not Process The Image You Requested.")    
    InitiateSearch()

InitiateSearch()