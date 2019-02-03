import flask
import subprocess
import settings
from database import dbHandler
from server.__main__ import app

if __name__ == '__main__':
	app.run(host=settings.host, port=settings.port, debug=True)
