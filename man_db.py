import sqlite3
import os

class man:

	def __init__(self):
		if not os.path.exists("index.db"):
			self.create_db()

	def create_db(self):
		conn = sqlite3.connect("index.db")
		c = conn.cursor()
		sql = "CREATE TABLE urls(Url TEXT, Sheme TEXT)"
		c.execute(sql)
		conn.commit()
		conn.close()
		
	def write(self, url, sheme):
		conn = sqlite3.connect("index.db")
		c = conn.cursor()
		sql = "INSERT INTO urls(Url, Sheme) VALUES ('" + str(url) + "', '" + str(sheme) + "')"
		c.execute(sql)
		conn.commit()
		conn.close()
		
	def read(self, sql):
		conn = sqlite3.connect("index.db")
		c = conn.cursor()
		c.execute(sql)
		items = c.fetchall()
		conn.close()
		return(items)