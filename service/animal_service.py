from typing import List

from domain.animal import Animal
from domain.exceptions import EmptyExceptions
from repository.in_memory_repository import Repository


class AnimalService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def get_animal(self, animal_name):
        animals = self.__repository.read()
        for animal in animals:
            if animal.get_name() == animal_name:
                return animal
        return None

    def add_animal(self, animal: Animal) -> bool:
        return self.__repository.create(animal)

    def delete_animal(self, animal: Animal) -> bool:
        return self.__repository.delete(animal)

    def get_all_animals(self) -> List[Animal]:
        return self.__repository.read()


