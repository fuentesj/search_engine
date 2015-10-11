import re
import urllib2
from BeautifulSoup import BeautifulSoup

class SearchEngine:

	def __init__(self):
		self.seed_urls = []

	def search(self, seed_url):
		self.__fetch_disallowed_paths(seed_url)
		html_page = urllib2.urlopen(seed_url)
		soup = BeautifulSoup(html_page)
		for link in soup.findAll('a'):
			print link.get('href')

	def __fetch_disallowed_paths(self, base_url):
		robots_txt = urllib2.urlopen(base_url + "/robots.txt")
		print robots_txt
		#disallowed_paths = re.findall(r'Disallow:*', robots_txt)
		#print "Disallowed paths"
		#print disallowed_paths
