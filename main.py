import os
import pytube
from pytube import YouTube
from pytube.exceptions import RegexMatchError


def download_video(url: str):
    try:
        print("Downloading...")
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True).desc().first()
        title = video.title
        video.download("/Videos", filename=f"{video.title}.mp4")
        print("Downloaded!")
        return "SUCCESS", title
    except RegexMatchError:
        print("Invalid URL")
        return "ERROR"
    except pytube.exceptions.AgeRestrictedError:
        print("This Content is age restricted and can't be accessed")
        return "ERROR"


while True:
    returned = download_video(input("YT URL: "))
    if returned[0] == "SUCCESS":
        os.system('"' + f'/Videos/{returned[1]}.mp4' + '"')

