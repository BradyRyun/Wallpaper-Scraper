# Wallpaper-for-GH
Script that scrapes the r/wallpaper subreddit and saves the images.

# Getting Setup
- Please checkout the following link before getting started: [How to Scrape Reddit](https://www.storybench.org/how-to-scrape-reddit-with-python/)
1. You will need to have an account on Reddit. Follow the above link's guide and replace the following code with your information. All of which are string values. 

```
client_id="SCRIPT_ID",
client_secret="CLIENT_SECRET_KEY",
user_agent="SCRIPT_NAME",
username="REDDIT_USERNAME",
password="REDDIT_PASSWORD",
```

2. Next, replace the `dir` variable in both the `wallpaperscraper.py` & `setRandomWallpaper.py` files.
3. Run `python wallpaperscraper.py` to gather all your background images.
4. run `python setRandomWallpaper.py` to set a random wallpaper from the downloaded images.
