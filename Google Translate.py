#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：dataTransfer
@File ：Google Translate.py
@Author ：ninesun
@Date ：2022/11/18 8:43
@Desc:
'''

import os
from concurrent.futures import ThreadPoolExecutor
# from pyperclip import copy

os.system('title 查找最佳的谷歌翻译IP')

ipAndSpeed = []

ips = '''
142.250.4.90
172.253.114.90
172.217.203.90
172.253.112.90
142.250.9.90
172.253.116.90
142.250.97.90
142.250.30.90
142.250.111.90
172.217.215.90
142.250.11.90
142.251.9.90
108.177.122.90
142.250.96.90
142.250.100.90
142.250.110.90
172.217.214.90
172.217.222.90
142.250.31.90
142.250.126.90
142.250.10.90
172.217.195.90
172.253.115.90
142.251.5.90
142.250.136.90
142.250.12.90
142.250.101.90
172.217.192.90
142.250.0.90
142.250.107.90
172.217.204.90
142.250.28.90
142.250.125.90
172.253.124.90
142.250.8.90
142.250.128.90
142.250.112.90
142.250.27.90
142.250.105.90
172.253.126.90
172.253.123.90
172.253.62.90
142.250.98.90
172.253.113.90
'''


def ipList():
    '''获取IP地址'''
    return { i.strip() for i in ips.splitlines() if i.strip() }


def pingInfo(ip):
    '''ping Ip 获取ms 最终取最小值'''
    cmd = f'ping /n 1 {ip}'
    for echoTxt in os.popen(cmd):
        if '请求超时。' in echoTxt:
            ipAndSpeed.append([ip, 999])
            print(ip, '超时')
            return
        if echoTxt := echoTxt.strip():# 去掉头尾的空格
            echoTxt = echoTxt.replace(' ', '') # 去掉字符串中间的空格，结合ping的结果来理解
            if '，平均=' in echoTxt:
                ms = int(echoTxt.split('=')[-1].replace('ms', ''))  # 分割平均=xxms
                ipAndSpeed.append([ip, ms])
                print(ip, f'{ms}ms')
                return


def fastScan():
    with ThreadPoolExecutor(20) as Pool:  #使用线程池，设置20个线程，可修改
        Pool.map(pingInfo, ipList())


fastScan()

sortedSpeed = sorted(ipAndSpeed, key=lambda x: x[-1]) # 按照延迟大小升序排序
for n, i in enumerate(sortedSpeed, 1): # 将一个sortedSpeed数据对象组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。 此例当中下标从1开始
    i[-1] = '超时' if i[-1] == 999 else f'{i[-1]}ms'
    print(f'【{str(n).zfill(2)}】\t{i[0]}\t {i[1]}') # zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。

fastip, ms = sortedSpeed[0]
print(f'\n最佳IP是：【{fastip}】，响应时间：【{ms}】')




# copy(hostTxt)
# print(f'\n\n设置hosts的内容“已复制到剪贴板”：   {hostTxt}\n\n\n按【任意键】打开hosts目录，然后【手动】修改。',
#       end='')
#
# os.system('pause>nul')
# os.popen('explorer /select,C:\Windows\System32\drivers\etc\hosts')

