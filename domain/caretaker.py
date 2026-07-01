from domain.animal import Animal


class Caretaker:
    def __init__(self, name, age, animal: Animal):
        self.__name = name
        self.__age = age
        self.__animal = animal

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def get_animal(self):
        return self.__animal

    def set_animal(self, new_animal):
        self.__animal = new_animal

    def __str__(self):
        return "Name: {0}, Age: {1}, Animal name: {2}".format(self.__name, self.__age, self.__animal.get_name())

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.get_name() == other.get_name()
                and self.get_age() == other.get_age()
                and self.get_animal() == other.get_animal())