import server.server.app as application
from server import settings

activate_this = {settings.python_path}
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
