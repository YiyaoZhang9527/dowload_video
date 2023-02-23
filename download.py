import subprocess
import os
import re
from log_color import log,LogLevel

def check_video(url):
    cmd = f"you-get -i {url}"
    status , output = subprocess.getstatusoutput(cmd)
    if status == 0:
        print(f"[视频检测结果]\n{output}",LogLevel.INFO)
        # print(f"status:[{status}]\noutput:[{output}]")
        size_list = [int(byte) for byte in re.findall(r"\((.*?) bytes\)",output)]
        download_cmd = re.findall(r"# download-with: \x1b\[4m(.*?) \[URL\]",output)
        max_size_index = size_list.index(max(size_list))
        log(f"[视频大小列表]:\n{size_list}",LogLevel.INFO)
        log(f"[最大视频大小]:\n{max_size_index}",LogLevel.INFO)
        log(f"[视频下载命令头列表]:\n{download_cmd}",LogLevel.INFO)
        header = download_cmd[max_size_index]
        return header
        

    

def download_from_url(url,filename=False,location_path=os.getcwd()):
    header = check_video(url)
    # if isinstance(filename,str):
    #     init_filename = f"-O {filename} "
    # else:
    init_filename = isinstance(filename,str) and f"-O {filename} " or " "
    log(f"[保存文件名]\n{init_filename}",LogLevel.INFO)
    download_cmd = f"{header} -o {location_path}{os.sep} {init_filename}{url}" 
    
    log(f"[下载命令]:\n{download_cmd}",LogLevel.INFO)
    
    try:
        os.system(download_cmd)
    except Exception as err:
        log(err,LogLevel.ERROR)
        os.system(download_cmd)
        


def batch_download(start_url,start_step,max_step,filename=False):
    
    for i in range(start_step,max_step+1):
        url = f"{start_url}{i}"
        log(f"\n<正在下载的url>\n{url}\n",LogLevel.PASS)
        download_from_url(url,filename != False and f"{filename}_{i}" or False)
        
        
    
    
    
    
if __name__ == '__main__':
    #print(check_video("https://www.bilibili.com/video/av472769223/?p=16"))
    #print(download_from_url("https://www.bilibili.com/video/av472769223/?p=16",filename="熬了一晚上我从零实现了Transformer模型"))
    batch_download("https://www.bilibili.com/video/av472769223/?p=",1,55)