import sqlite3
import os

class man:

	def __init__(self):
		if not os.path.exists("index.db"):
			self.create_db()

	def create_db(self):
		conn = sqlite3.connect("index.db")
		c = conn.cursor()
		sql = "CREATE TABLE urls(Url TEXT)"
		c.execute(sql)
		conn.commit()
		conn.close()
		
	def write(self, url):
		conn = sqlite3.connect("index.db")
		c = conn.cursor()
		sql = "INSERT INTO urls(Url) VALUES ( '" + str(url) + "')"
		c.execute(sql)
		conn.commit()
		conn.close()
		
	def read(self, search):
		conn = sqlite3.connect("index.db")
		c = conn.cursor()
		sql = "SELECT * from urls where Url LIKE " + str(search)
		c.execute(sql)
		items = c.fetchall()
		conn.close()
		return(items)