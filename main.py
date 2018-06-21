import sys
import os
from spider import Spider
from pdf import create_pdf

url = sys.argv[1]

spider = Spider(url)

print('书名：', spider.book.name)
print('作者：', spider.book.author)
print('类型：', spider.book.bookType)
print('简介：', spider.book.description)

isExist = os.path.exists(spider.book.name)
if not isExist:
    print('{0}文件夹不存在，自动创建...'.format(spider.book.name))
    os.makedirs(spider.book.name)
    print('{0}文件夹创建成功！'.format(spider.book.name))

for p in spider.book.content:
    story = p['part'] + '\n' + '---------------' + '\n'
    print(story)
    for charpter in p['charpters']:
        story += charpter['title'] + '\n' + \
            charpter['content'] + '\n' + '---------------' + '\n'

    filePath = '{0}/{1}.pdf'.format(spider.book.name.strip(),
                                    p['part'].strip())
    create_pdf(story, filePath)

print('pdf导出完成')
