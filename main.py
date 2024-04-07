import os
import pytube
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import os
import string
import random


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def download_video(url: str):
    try:
        print("Downloading...")
        yt = YouTube(url)
        file = id_generator(10)
        video = yt.streams.filter(progressive=True).desc().first()
        video.download("./Videos", filename_prefix=f"{file}", filename=f".mp4")
        print("Downloaded!")
        return "SUCCESS", file
    except RegexMatchError:
        print("Invalid URL")
        return "ERROR"
    except pytube.exceptions.AgeRestrictedError:
        print("This Content is age restricted and can't be accessed")
        return "ERROR"


while True:
    returned = download_video(input("YT URL: "))
    if returned[0] == "SUCCESS":
        os.system('"' + f'.\\Videos\\{returned[1]}.mp4' + '"')

