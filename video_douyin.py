#!/usr/bin/env python
"# -*- encoding: utf-8 -*-"
'''
@File  :  video_douyin.py
@Author:  manman
@Date  :  2020/11/214:32 上午
@Desc  :  https://blog.csdn.net/qq_44700693/article/details/108089085?utm_source=app
@File  :  
@Time  :  // ::",
@Contact :   408903228@qq.com
@Department   :  my-self
'''
import requests
import re
import random
import os
path = os.path.expanduser("~/crawlers_001/video/douyin/")

class DY():  # 抖音
    headers = {  # 模拟手机端
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/84.0.4147.105'
    }

    def __init__(self, s_url):
        self.url = re.findall('(https?://[^\s]+)', s_url)[0]  # 正则提取字符串中的链接

    def dy_download(self):
        rel_url = str(requests.get(self.url, proxies=proxy, headers=self.headers).url)
        if 'video' == rel_url.split('/')[4]:
            URL = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + rel_url.split('/')[5] + '&dytk='
            r = requests.get(URL, proxies=proxy, headers=self.headers)
            video_url = r.json()['item_list'][0]['video']['play_addr']['url_list'][0].replace('/playwm/', '/play/')
            video_name = r.json()['item_list'][0]['share_info']['share_title'].split('#')[0].split('@')[0].replace(' ','')
            if video_name == '':
                video_name = int(random.random() * 2 * 1000)
            if len(str(video_name)) > 20:
                video_name = video_name[:20]
            video = requests.get(video_url, proxies=None, headers=self.headers).content
            with open(path + str(video_name) + '.mp4', 'wb') as f:
                f.write(video)
            print("【抖音短视频】: {}.mp4 无水印视频下载完成！".format(video_name))#".format(video_name))
            if 'www.iesdouyin.com' in self.s_url:
                print("【抖音短视频】: {}.mp4 无水印视频下载完成！".format(video_name))
            if 'v.douyin.com' in self.s_url:
                print("【抖音短视频/抖音极速版】: {}.mp4 无水印视频下载完成！".format(video_name))


if __name__ == '__main__':
    proxy = None
    print("请输入网址:")
    url="http://v26-dy.ixigua.com/530f80c138b2f2a1568663e5b09085b7/5fb838ba/video/tos/cn/tos-cn-ve-15/eadade12cd454be9a0bf0c32861abf3a/?a=1128&br=4389&bt=1463&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20201121044340010198062140484E7D51&lr=aweme_search_suffix&mime_type=video_mp4&qs=0&rc=amdwcm9kc2dqdjMzOGkzM0ApaDlkOGhoZGVpN2Q1ZTo1N2c1bjFrZGVtcGJfLS00LS9zc18zLjAtNTBiL2ItMWAtYC86Yw%3D%3D&vl=&vr="
    DY().dy_download()

