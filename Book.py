class Book:
    def __init__(self):
        self.name = ''
        self.author = ''
        self.bookType = ''
        self.description = ''
        self.content = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAuthor(self, author):
        self.author = author

    def getAuthor(self):
        return self.author

    def setBookType(self, bookType):
        self.bookType = bookType

    def getBookType(self):
        return self.bookType

    def setDescription(self, description):
        self.description = description

    def getDescriptions(self):
        return self.description

    def setContent(self, part, charpters):
        content = {'part': part, 'charpters': charpters}
        self.content.append(content)

    def getContent(self):
        return self.content
