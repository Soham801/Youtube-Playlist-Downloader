#Complete YT Playlist Downloader

from pytube import Playlist


p = Playlist("https://youtube.com/playlist?list=PLlzmAWV2yTgCjoZNF3hLX3puYJir9vSQO&si=-QDBq2j9qZL08IHh")

for video in p.videos:
    video.streams.first().download()