import flask
from server import app
import settings
from database import dbHandler
import subprocess

if __name__ == '__main__':
	app.run(host=settings.host, port=settings.port, debug=True)
