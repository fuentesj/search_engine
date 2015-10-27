import re
import urllib2
from BeautifulSoup import BeautifulSoup

class WebCrawler:

	def __init__(self):
		self.seed_urls = []
		self.inclusion_dict = {}
		self.ALLOW_KEYWORD = "Allow:"

	def search(self, seed_url):
		self.__fetch_disallowed_paths(seed_url)
		html_page = urllib2.urlopen(seed_url)
		soup = BeautifulSoup(html_page)
		for link in soup.findAll('a'):
			print link.get('href')

	def fetch_allowed_paths(self, base_url):
		http_response = urllib2.urlopen(base_url + "/robots.txt")
		response_data = http_response.read()
		robots_exclusion_list = response_data.split('\n');
		for entry in robots_exclusion_list:
			action_match = re.search('.+:', entry)
			if action_match:
			 	action = action_match.group(0) 
			 	if action == self.ALLOW_KEYWORD:
					path_match = re.search('\/.+', entry)
					path = path_match.group(0)
					self.inclusion_dict[path] = action