class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f"Animal: {self.__name} Age: {self.__age}"

    def __eq__(self, value, /):
        return self.__name == value

