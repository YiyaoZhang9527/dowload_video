import subprocess
import os
from weakref import proxy


import youtube_dl

def load_address(txt_file):
    return [url for url in open(txt_file).readlines() if len(url) > 0 and "http" in url]

def get_video(url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            url,
            download=True # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result
        
    print(video)
    video_url = video['url']
    print("video_url:",video_url)
    
    
if __name__ == '__main__':
    No = 0
    for url in load_address("/home/zhangmanman/Videos/YX/url"):
        No += 1
        try:
            get_video(url)
        except Exception as e:
            get_video(url)
        finally:

            print(f"已经下载第{No}个")
        
