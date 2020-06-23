import ctypes
import random as rand
import os

SPI_SETDESKWALLPAPER = 20 
imageNumber = str(rand.randint(1, 92))
image_name = "image_" + imageNumber + ".jpg";
# Use absolute path to desired folder holding your background images
dir = "C:/Users/Username/Pictures/Backgrounds/"
path = dir + image_name;

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)