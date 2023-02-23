import os
import re
from log_color import log,LogLevel

def getfileID(share_link):
        # 使用正则表达式模式匹配 d/ 和 /view? 之间的内容
    match = re.search(r"d/(\w+).*?/view\?", share_link)

    # 如果找到匹配项，则提取内容
    if match:
        content = match.group(1)
        return content
    else:
        print("No match found.")

def get_download_cmd(FILEID,FILENAME):
    handler = 'wget --load-cookies /tmp/cookies.txt "'
    body = f"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id={FILEID}' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p')&id={FILEID}" 
    end = f'" -O {FILENAME} && rm -rf /tmp/cookies.txt'
    cmd = f"{handler}{body}{end}"
    log(f"谷歌硬盘分享wget下载命令是:\n[ {cmd} ]",LogLevel.PASS)
    return cmd



if __name__ == '__main__':

    print(get_download_cmd(getfileID("https://drive.google.com/file/d/1Epz2WweALXPlLYRaaTdWT6nMOBjkqWk0/view?usp=share_link"),"RescueNet.zip"))