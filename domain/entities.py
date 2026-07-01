class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __eq__(self, other):
        return self.get_name() == other.get_name() and self.get_age() == other.get_age()

    def __str__(self):
        return f'Name: {self.__name}, age: {self.__age}'

    def __repr__(self):
        return str(self)

