import re
import urllib2
from bs4 import BeautifulSoup

class WebCrawler:

	def __init__(self):
		self.seed_urls = []
		self.allowed_paths_list = []
		self.ALLOW_KEYWORD = "Allow:"

	def search(self, base_domain):
		try:
			self.fetch_allowed_paths(base_domain)
			for path in self.allowed_paths_list:
				try:
				 	html = urllib2.urlopen(base_domain+path)
				 	soup = BeautifulSoup(html)
					if soup is not None:
						print soup.find_all('a')
				except urllib2.HTTPError, error:
					print "An exception with an error code " + str(error.code) + " occurred while crawling " + base_domain + path
		except urllib2.HTTPError:
			print "No robots.txt was found! Exiting now."
		

	def fetch_allowed_paths(self, base_domain):
		http_response = urllib2.urlopen(base_domain + "/robots.txt")
		response_data = http_response.read()
		robots_exclusion_list = response_data.split('\n');
		for entry in robots_exclusion_list:
			action_match = re.search('.+:', entry)
			if action_match:
			 	action = action_match.group(0) 
			 	if action == self.ALLOW_KEYWORD:
					path_match = re.search('\/.+', entry)
					path = path_match.group(0)
					self.allowed_paths_list.append(path)