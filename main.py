from service.animal_service import AnimalService
from ui.ui import UI
from domain.animal import Animal
from repository.in_memory_repository import Repository


animal_repository = Repository([Animal("Rex", 12), Animal("Banana", 2)])
service = AnimalService(animal_repository)

ui = UI(service)

ui.run()

