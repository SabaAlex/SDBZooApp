from domain.animal import Animal
from repository.in_memory_repository import Repository
from typing import List

from domain.caretaker import Caretaker

class CaretakerService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_caretaker(self, caretaker: Caretaker) -> bool:
        return self.__repository.create(caretaker)

    def delete_caretaker(self, caretaker: Caretaker) -> bool:
        return self.__repository.delete(caretaker)

    def get_all_caretakers(self) -> List[Caretaker]:
        return self.__repository.read()

    def specific_animal(self, animal: Animal) -> bool:
        caretakers = self.get_all_caretakers()
        for caretaker in caretakers:
            if caretaker.get_animal() == animal:
                return True
        return False
