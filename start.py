import flask
from server import server, settings
from database import dbHandler
import subprocess

def main():
	subprocess.run(['pip', 'install', '-r', 'requirements.txt', '--quiet'])
	server.app.run(host=settings.host, port=settings.port, debug=settings.debug)

if __name__ == '__main__':
	main()
