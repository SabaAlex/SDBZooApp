from typing import List

from domain.animal import Animal
from domain.exceptions import EmptyExceptions
from repository.in_memory_repository import Repository


class AnimalService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_animal(self, animal: Animal) -> bool:
        return self.__repository.create(animal)

    def delete_animal(self, animal: Animal) -> bool:
        return self.__repository.delete(animal)

    def get_all_animals(self) -> List[Animal]:
        return self.__repository.read()

    def average_age(self) -> float:
        animals = self.__repository.read()
        if len(animals) == 0:
            raise EmptyExceptions("Collection is empty")

        age_sum = 0
        for animal in animals:
            age_sum += animal.get_age()

        median = age_sum / len(animals)

        return median
