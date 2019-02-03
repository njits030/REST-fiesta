################################################################################
# Imports
################################################################################

import flask, json, markdown
from database import dbHandler
from flask.views import View

################################################################################
# Setting up the app and the handler
################################################################################

db = dbHandler.handler()
app = flask.Flask(__name__)

################################################################################
# Get data from the database
################################################################################

@app.route('/', methods = ["GET"])
@app.route('/retrieve', methods = ["GET"])
def retrieve():
	data = db.get_all()
	if data == None:
		return "No data found", 404
	return json.dumps(data), 200

@app.route('/<int:id>', methods = ["GET"])
@app.route('/retrieve/<int:id>', methods = ["GET"])
def retrieveSpecific(id):
	data = db.get_one(id)
	if data == None:
		return f"No data found for ID {id}", 404
	return json.dumps(data), 200

################################################################################
# Post data to the database
################################################################################

@app.route('/', methods = ["POST"])
@app.route('/post', methods = ["POST"])
def post():
	requestData = flask.request.json
	data = db.post(requestData)
	return json.dumps(data), 201

@app.route('/<int:id>', methods = ["PUT"])
@app.route('/post/<int:id>', methods = ["PUT"])
def put(id):
	requestData = flask.request.json
	data = db.put(requestData, id)
	return json.dumps(data), 201

################################################################################
# Delete data from the database
################################################################################

@app.route('/reset', methods = ["DELETE"])
def reset():
	db.reset()
	return f"Table data reset", 204

@app.route('/<int:id>', methods = ["DELETE"])
@app.route('/delete/<int:id>', methods = ["DELETE"])
def delete(id):
	db.delete_one(id)
	return f"Deleted entry {id}", 204

################################################################################
# Display documentation
################################################################################
@app.route('/help', methods = ["GET"])
def displayHelp():
	content = markdown.markdown(open('README.md'))
	return content, 200

################################################################################
# Error handling
################################################################################
