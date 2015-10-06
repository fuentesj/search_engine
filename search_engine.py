import urllib2
from BeautifulSoup import BeautifulSoup

class SearchEngine:

	def __init__(self):
		self.seed_urls = []

	def search(self, seed_url):
		html_page = urllib2.urlopen(seed_url)
		soup = BeautifulSoup(html_page)
		for link in soup.findAll('a'):
			print link.get('href')