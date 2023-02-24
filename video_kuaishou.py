#!/usr/bin/env python
"# -*- encoding: utf-8 -*-"
'''
@File  :  video_kuaishou.py
@Author:  manman
@Date  :  2020/11/214:03 上午
@Desc  :  https://blog.csdn.net/qq_44700693/article/details/108089085
@File  :  
@Time  :  // ::",
@Contact :   408903228@qq.com
@Department   :  my-self
'''
import requests
import re
import random
import os
path = os.path.expanduser("~/crawlers_001/video/kuaishou/")

class KS():  # 快手
    def __init__(self, s_url):
        self.s_url=s_url.replace('\n','').split('/')[-1]
        self.url = re.findall('(https?://[^\s]+)', s_url)[0]  # 正则提取字符串中的链接
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/84.0.4147.105'
        }

    def ks_download(self):
        No = self.s_url.split("/u")[-1]
        html = requests.get(self.url, headers=self.headers).text
        video_name = re.findall('name":"(.*?)"', html)[0].replace(' ','')
        if video_name == '':
            video_name = int(random.random() * 2 * 1000)
        if len(str(video_name)) > 20:
            video_name = video_name[:20]
        video_url = re.findall('srcNoMark":"(.*?)"', html)[0]
        video = requests.get(video_url, proxies=None, headers=self.headers).content
        with open(path + str(video_name) + No+'.mp4', 'wb') as f:
            f.write(video)
        if '【快手App】' in self.s_url:
            print("【快手】: {}.mp4 无水印视频下载完成！".format(video_name))
        elif '【快手极速版App】' in self.s_url:
            print("【快手极速版】: {}.mp4 无水印视频下载完成！".format(video_name))

if __name__ == '__main__':
    path = os.path.expanduser("~/Documents/crawlers_001/video/kuaishou/")
    print("输入视频网址:")
    url = input()
    KS(url).ks_download()

