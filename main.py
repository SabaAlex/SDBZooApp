from domain.caretaker import Caretaker
from service.animal_service import AnimalService
from service.caretaker_service import CaretakerService
from service.statistics_service import StatisticsService
from ui.ui import UI
from domain.animal import Animal
from repository.in_memory_repository import Repository

animals = [Animal("Rex", 12), Animal("Banana", 2)]
animal_repository = Repository(animals)
caretaker_repository = Repository([Caretaker("Radu", 20, animals[0])])

animal_service = AnimalService(animal_repository)
caretaker_service = CaretakerService(caretaker_repository)
statistics_service = StatisticsService(animal_service, caretaker_service)

ui = UI(animal_service, caretaker_service, statistics_service)

ui.run()

