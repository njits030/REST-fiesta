################################################################################
# Imports
################################################################################

import sqlite3
from server import settings

################################################################################
# Class for handling the database
################################################################################

class handler(object):
	dbFile = f"{settings.databaseFile}"

	def init_db(self):
		db = sqlite3.connect(self.dbFile)
		db.cursor().execute(f"CREATE TABLE IF NOT EXISTS {settings.tableName} (ID INTEGER PRIMARY KEY AUTOINCREMENT);")
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
		db.cursor().execute(f"SELECT * FROM {settings.tableName};")
		data = db.cursor().fetchall()
		db.commit()
		db.close()

		return data

	def get_one(self, id):
		db = self.connect_db()
		db.cursor().execute(f"SELECT * FROM {settings.tableName} WHERE ID = ?;", (id, ))
		data = db.cursor().fetchone()
		db.commit()
		db.close()

		return data

	def delete_one(self, id):
		db = self.connect_db()
		db.cursor().execute(f"DELETE FROM {settings.tableName} WHERE ID = ?;", (id, ))
		db.commit()
		db.close()

		return

	def reset(self, id):
		db = self.connect_db()
		db.cursor().execute(f"DROP TABLE {settings.tableName};")
		self.init_db()

		return
