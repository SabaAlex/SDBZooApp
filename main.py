from service import Service
from ui import UI

service = Service()
ui = UI(service)

ui.run()