from service import AnimalServices
from ui import UI
from entities import Animal

service = AnimalServices()
service.add_animal(Animal("Rex", 12))
service.add_animal(Animal("Banana", 2))

ui = UI(service)

ui.run()

