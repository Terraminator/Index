import requests
import man_db
import bs4
from urllib.request import Request, urlopen
import re


class IndexSpider:

	def __init__(self):
		self.man = man_db.man()
		self.urls = [
			'https://www.wikipedia.com',
			#'https://en.wikipedia.com/wiki/Wikipedia:Contents/A%E2%80%93Z_index'
			#'https://www.google.com',
			#'https://www.perspektiven-finden.com/unternehmen.com',
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
				link = link.get('href')
				if not link in self.urls:
					if not "http" in link:
						if link =="/%s":
							link = url.split(".%s/")[0] + url.split(".com/")[1] + link
						else:
							link = url.split("//")[0] + link
					self.urls.append(link)
					print(link)

		except:
			pass

			
	def parse(self, url):
		#try:
		self.get_links(url)
		if "http" in url:
			self.man.write(url)
		#except:
		#	pass

if __name__ == "__main__":
	indexspider = IndexSpider()