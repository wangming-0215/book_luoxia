import sys

from spider import Spider

from pdf import create_pdf

# url = sys.argv[1]

spider = Spider()

print('书名：', spider.book.name)
print('作者：', spider.book.author)
print('类型：', spider.book.bookType)
print('简介：', spider.book.description)
# print(spider.book.content)


for p in spider.book.content:
    story = p['part'] + '\n' + '---------------'
    print(story)
    for charpter in p['charpters']:
        story += charpter['title'] + '\n' + \
            charpter['content'] + '\n' + '---------------'

    create_pdf(story, p['part'] + '.pdf')
