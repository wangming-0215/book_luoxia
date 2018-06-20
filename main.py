import sys

from spider import Spider

url = sys.argv[1]

spider = Spider(url)

print('书名：', spider.book.name)
print('作者：', spider.book.author)
print('类型：', spider.book.bookType)
print('简介：', spider.book.description)
print(spider.book.content)
