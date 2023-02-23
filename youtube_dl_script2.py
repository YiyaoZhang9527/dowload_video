import youtube_dl
from log_color import  log,LogLevel

def load_address(txt_file):
    return [url for url in open(txt_file).readlines() if len(url) > 0 and "http" in url]

def download_video(url,download_path="/home/zhangmanman/Videos/YX/"):
    ydl_opts = {
        'outtmpl': f'{download_path}%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'proxy':'socks5://127.0.0.1:7890'
    }
    

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            ydl.download([url])
        finally:
            log(url,LogLevel.INFO)
            

def download_videos(filepath,history_log="/home/zhangmanman/Videos/url_history"):
    histroy_urls = open(history_log).readlines()
    
    No = 0
    for url in load_address(filepath):
        No += 1
        if url in histroy_urls:
            log(f"{url}已经在下载历史中了了，当前是本轮第{No}个视频",LogLevel.INFO)
        else:
            try:
                download_video(url)
            except Exception as e:
                download_videos(url)
            finally:
                log(f"已经下载第{No}个",LogLevel.INFO)
                history_file = open(history_log,"a+")
                history_file.write(f"{url}\n")
                history_file.close()
                log(f"已经将url加入下载历史",LogLevel.PASS)




if __name__ == '__main__':
    download_videos("/home/zhangmanman/Videos/YX/url2")