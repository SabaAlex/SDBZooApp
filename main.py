from ZooApp.service import Service
from ZooApp.ui import UI

service = Service()
ui = UI(service)

ui.run()