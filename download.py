from pytube import YouTube
from moviepy.editor import *

file = open('list.txt', 'r')

for line in file:
    url = line
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download()
