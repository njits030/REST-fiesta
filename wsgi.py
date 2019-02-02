from server import server
from server import settings
import sys

application = server.app

activate_this = settings.python_path
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.insert(0, settings.app_path)
