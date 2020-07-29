# Wallpaper-Scraper
Script that scrapes the r/wallpaper subreddit and saves the images.

# Getting Setup
- Please checkout the following link before getting started: [How to Scrape Reddit](https://www.storybench.org/how-to-scrape-reddit-with-python/)
## Required Dependencies
- If you do not have a dependency, use `pip install dependency` to install the following:
  - Praw
  - BeautifulSoup
  - requests
## Adjust Values
1. You will need to have an account on Reddit. Follow the above link's guide and replace the following code with your information. All of which are string values. 

```
client_id="SCRIPT_ID",
client_secret="CLIENT_SECRET_KEY",
user_agent="SCRIPT_NAME",
username="REDDIT_USERNAME",
password="REDDIT_PASSWORD",
```

2. Next, replace the `dir` variable in both the `wallpaperscraper.py` & `setRandomWallpaper.py` files with the absolute path to the folder you'd like to save the wallpapers to. 
3. Run `python wallpaperscraper.py` to gather all your background images.
4. Run `python setRandomWallpaper.py` to set a random wallpaper from the downloaded images.
  - Alternatively, on Windows, you can right-click your background. Select "Personalize". Then change your background to "Slideshow" and choose the folder you're saving the files to to change pictures over a time interval. 
