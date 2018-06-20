import re
import requests
from bs4 import BeautifulSoup

from Config import Config
from Book import Book


class Spider:
    def __init__(self, url):
        self.config = Config(url)
        self.book = Book()
        self.session = requests.Session()
        self.html = self.getBookPage()
        self.main()

    def request(self, url):
        response = self.session.get(url, headers=self.config.headers)
        response.encoding = 'utf-8'  # 解决中文乱码
        return BeautifulSoup(response.text, 'html.parser')

    def getBookPage(self):
        html = self.request(self.config.url)
        return html

    def getBookDescription(self):
        description = self.html.find('div', attrs={'class': 'book-describe'})
        name = description.find('h1').text
        author, bookType, *_ = description.find_all('p')
        author = re.compile(r'作者：').sub('', author.text)
        bookType = re.compile(r'类型：').sub('', bookType.text)
        describe = description.find(
            'div', attrs={'class': 'describe-html'}).find('p').text
        return name, author, bookType, describe

    def getCharpterContent(self, url):
        html = self.request(url)
        content = html.find('div', attrs={'id': 'nr1'}).text
        return content

    def getBookCharpter(self):
        partsContainer = self.html.find_all(
            'div', attrs={'class': 'title clearfix'})

        partList = list(map(lambda x: re.compile(
            r'\n').sub(' ', x.text), partsContainer))

        chaptContainer = self.html.find_all(
            'div', attrs={'class': 'book-list'})

        contents = []

        for index, chapt in enumerate(chaptContainer):
            lis = chapt.find_all('li')
            charpters = []
            for _, li in enumerate(lis):
                title = re.compile(r'\u3000').sub(' ', li.text)
                aLink = li.find('a')
                url = ''

                if (aLink):
                    url = aLink.attrs['href']
                else:
                    b = li.find('b').attrs['onclick']
                    url = re.search(
                        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', b,  re.M | re.I).group()

                print(partList[index] + title)

                content = self.getCharpterContent(url)
                chapt = {'title': title, 'url': url, 'content': content}
                charpters.append(chapt)
            contents.append(charpters)
        return partList, contents

    def main(self):
        name, author, bookType, describe = self.getBookDescription()
        partList, contents = self.getBookCharpter()
        self.book.setName(name)
        self.book.setAuthor(author)
        self.book.setBookType(bookType)
        self.book.setDescription(describe)

        for index, item in enumerate(partList):
            self.book.setContent(item, contents[index])
