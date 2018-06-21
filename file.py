'''
1、读取指定目录下的所有文件
2、读取文件，正则匹配出需要的内容，获取文件名
3、打开此文件(可以选择打开可以选择复制到别的地方去)
'''
import os.path
import re


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    print(list(filter(lambda x: re.search(r'\.ttf$', x), pathDir)))


eachFile(r'C:\Windows\Fonts')
