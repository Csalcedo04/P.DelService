class Document(object):

    def __init__(self, id: int = 0, title: str = "title", pages: int = 0,
                 category: str = "category", author: str = "author"):
        self._id = id
        self._title = title
        self._pages = pages
        self._category = category
        self._author = author

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        self._pages = pages

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author: str):
        self._author = author

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}'.format(self.id, self.title, self.pages, self.category, self.author)


if __name__ == '__main__':
    C1 = Document(id=1010, title="le petit prince", pages="96", category="literatura infantil",
                  author="Antoine de Saint-Exupery")
    C2 = Document(id=1234, title="De cero a uno", pages="120", category="Negocios e inversiones",
                  author="Peter Thiel")
    print(p1)
    print(p2)
