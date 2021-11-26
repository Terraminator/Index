import requests
import man_db
import bs4
from urllib.request import Request, urlopen
import re


class IndexSpider:

	def __init__(self):
		self.man = man_db.man()
		self.urls = [
			#'https://www.wikipedia.com',
			#'https://en.wikipedia.com/wiki/Wikipedia:Contents/A%E2%80%93Z_index'
			#'https://www.google.com',
			'https://www.perspektiven-finden.com/unternehmen',
			]
		self.start_requests()
	
	def start_requests(self):
		while len(self.urls) > 0:
			for url in self.urls:
				self.parse(url)
		print(self.urls)
			
	def get_links(self, url):
		try:
			self.urls.remove(url)
			res = requests.get(url)
			soup = bs4.BeautifulSoup(res.text, "lxml")
			for link in soup.findAll('a'):
				try:
					link = link.get('href')
					if not "http" in link:
						if link[0] == '/':
							link = url.split(".%s/")[0] + url.split(".com/")[1] + link
						else:
							link = url.split("//")[0] + link
					if not link in self.urls:
						self.urls.append(link)
				except:
					pass

		except:
			pass

			
	def parse(self, url):
		self.get_links(url)
		if "www" in url:
			self.man.write(url)

if __name__ == "__main__":
	indexspider = IndexSpider()
