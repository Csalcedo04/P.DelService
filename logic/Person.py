class Person(object):

    def __init__(self, id: int = 0, name: str = "Name", last_name: str = "LastName", nationality: str = "nationality"):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._nationality= nationality

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def nationality(self):
        return self._nationality

    @id.setter
    def nationality(self, nationality: str):
        self._nationality = nationality

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.id, self.name, self.last_name, self.nationality)


if __name__ == '__main__':
    p1 = Person(id= 1010, name="Daniela", last_name="Franco", nationality= "alemania")
    p2 = Person(id= 1234, name="Laura", last_name="Zambrano", nationality= "francia")
    print(p1)
    print(p2)