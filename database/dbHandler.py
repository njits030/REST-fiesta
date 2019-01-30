################################################################################
# Imports
################################################################################

import sqlite3, json
from server import settings

################################################################################
# Class for handling the database
################################################################################

class handler(object):
	dbFile = f"{settings.databaseFile}"

	def init_db(self):
		db = sqlite3.connect(self.dbFile)
		db.cursor().execute(f"CREATE TABLE IF NOT EXISTS {settings.tableName} (ID INTEGER PRIMARY KEY AUTOINCREMENT, {self.genColTypes()});")
		db.commit()
		db.close()

	def connect_db(self):
		db = sqlite3.connect(self.dbFile)
		def dict_factory(cursor, row):
			dict = {}

			for idx, col in enumerate(cursor.description):
				dict[col[0]] = row[idx]

			return dict

		db.row_factory = dict_factory

		return db

	def get_all(self):
		db = self.connect_db()
		result = db.cursor().execute(f"SELECT * FROM {settings.tableName};")
		data = result.fetchall()
		db.commit()
		db.close()

		return data

	def get_one(self, id):
		db = self.connect_db()
		result = db.cursor().execute(f"SELECT * FROM {settings.tableName} WHERE ID = ?;", (id, ))
		data = result.fetchone()
		db.commit()
		db.close()

		return data

	def post(self, data):
		db = self.connect_db()
		db.cursor().execute(f"INSERT INTO {settings.tableName} ({self.genCols()}) VALUES ({self.genColData(data)});")
		db.commit()
		db.close()
		return data

	def put(self, data):
		return data

	def delete_one(self, id):
		db = self.connect_db()
		db.cursor().execute(f"DELETE FROM {settings.tableName} WHERE ID = ?;", (id, ))
		db.commit()
		db.close()

		return

	def reset(self):
		db = self.connect_db()
		db.cursor().execute(f"DROP TABLE {settings.tableName};")
		self.init_db()

		return

	def genCols(self):
		columns = ""

		for column in settings.columns:
			if column == list(settings.columns.keys())[-1]:
				columns += f"{column}"
			else:
				columns += f"{column}, "

		return columns

	def genColTypes(self):
		columns = ""

		for column in settings.columns:
			if column == list(settings.columns.keys())[-1]:
				columns += f"{column} {settings.columns[column]}"
			else:
				columns += f"{column} {settings.columns[column]}, "

		return columns

	def genColData(self, data):
		dataReturn = ""
		for value in data:
			if value == list(data.keys())[-1]:
				if type(value) != 'int':
					dataReturn += f"'{data[value]}'"
				else:
					dataReturn += f"{data[value]}"
			else:
				if type(value) != 'int':
					dataReturn += f"'{data[value]}', "
				else:
					dataReturn += f"{data[value]}, "
		return dataReturn
