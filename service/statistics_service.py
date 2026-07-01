from domain.caretaker import Caretaker
from domain.exceptions import EmptyExceptions
from service.animal_service import AnimalService
from service.caretaker_service import CaretakerService


class StatisticsService:
    def __init__(self, animal_service: AnimalService, caretaker_service: CaretakerService):
        self.__animal_service = animal_service
        self.__caretaker_service = caretaker_service

    def __average_age(self, entity_type) -> float:
        entities = []
        if entity_type == 'animal':
            entities = self.__animal_service.get_all_animals()
        elif entity_type == 'caretaker':
            entities = self.__caretaker_service.get_all_caretakers()
        if len(entities) == 0:
            raise EmptyExceptions("Collection is empty")

        age_sum = 0
        for entity in entities:
            age_sum += entity.get_age()

        median = age_sum / len(entities)

        return median

    def average_age_animals(self):
        self.__average_age('animal')

    def average_age_caretakers(self):
        self.__average_age('caretaker')

    def animals_without_caretaker(self):
        animals = self.__animal_service.get_all_animals()
        animals_without_caretaker = []
        for animal in animals:
            if not self.__caretaker_service.specific_animal(animal):
                animals_without_caretaker.append(animal)
        return animals_without_caretaker