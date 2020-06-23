import praw
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import quote
import requests
import sys
import os
import ctypes
import random

dir = "/Users/Username/Pictures/Backgrounds"
os.chdir(dir)
print("Navigated to directory...")

NUM_IMAGES = 100
batchNum = 1

# Creates a history folder if you do not already have one and creates a batch folder within it. 
if(os.path.isdir("History") == False):
    os.makedirs("History")
while (os.path.isdir(f"History/Batch_{batchNum}") == True):
    batchNum = batchNum + 1
os.makedirs(f"History/Batch_{batchNum}")
print("Batch number: " + str(batchNum) + " has been created")

reddit = praw.Reddit(
    client_id="SCRIPT_ID",
    client_secret="CLIENT_SECRET_KEY",
    user_agent="SCRIPT_NAME",
    username="REDDIT_USERNAME",
    password="REDDIT_PASSWORD",
)

#Select the wallpaper subreddit
subreddit = reddit.subreddit("wallpaper")

links = []

#Adds links from the hot portion of the subreddit.
for submission in subreddit.hot(limit=NUM_IMAGES):
    links.append("https://reddit.com" + submission.permalink)


images = []
for i in range(len(links)):
    sys.stdout.write(f"\rProcessing image {i+1} of {NUM_IMAGES}.")

    link_decoded = links[i][:21] + quote(links[i][21:])

    req = Request(link_decoded, headers={"User-Agent": "Mozilla/5.0"})
    
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    for link in soup.findAll("a"):

        if (
            "https://i.redd.it/" in str(link.get("href"))[0:18]
            and str(link.get("href")) not in images
        ):
            images.append(link.get("href"))
# Writes the images to the folder
for i in range(len(images)): 
    sys.stdout.write(f"\rWriting image {i+1}")
    img_data = requests.get(images[i]).content
    # If the image already exists in the main folder, moves it to the history folder with corresponding bathc number.
    if(os.path.isfile(f"image_{i+1}.jpg")):
        print("File name: " + f"image_{i+1}.jpg" + " already exists.")
        print("Moving file to history folder.")
        os.rename(f"image_{i+1}.jpg", f"History/Batch_{batchNum}/image_{i+1}.jpg")
    try:
        with open(f"image_{i+1}.jpg", "wb") as handler:
            handler.write(img_data)
            if os.stat(f"image_{i+1}.jpg").st_size < 200000:  # under 200 KB, too small for background image.
                handler.close()
                os.remove(f"image_{i+1}.jpg")
            handler.close()
    except WindowsError:
        print("Windows error occured. Moving to next file.")
