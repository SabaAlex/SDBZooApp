from typing import List
from entities import Animal
from exceptions import EmptyExceptions

class AnimalServices:
    def __init__(self):
        self.__animals = []

    def __animal_exists(self, animal_to_find: Animal) -> bool:
        for animal in self.__animals:
            if animal == animal_to_find:
                return True

        return False

    def add_animal(self, new_animal: Animal) -> bool:
        """
        This adds a new animal
        :param new_animal: the animal to be added
        :return: True if the animal was added false otherwise
        """
        if self.__animal_exists(new_animal):
            return False

        self.__animals.append(new_animal)
        return True

    def __find_position_of_animal(self, animal_to_find):
        animals = self.__animals
        for index in range(len(animals)):
            animal = animals[index]
            if animal == animal_to_find:
                return index

        return None

    def delete_animal(self, animal_to_delete: Animal) -> bool:
        position = self.__find_position_of_animal(animal_to_delete)

        if position is None:
            return False

        del self.__animals[position]
        return True

    def get_all_animals(self) -> List[Animal]:
        return self.__animals

    def average_age(self) -> float:
        if len(self.__animals) == 0:
            raise EmptyExceptions("Collection is empty")

        animals = self.__animals
        age_sum = 0
        for animal in animals:
            age_sum += animal.get_age()

        median = age_sum / len(animals)

        return median
