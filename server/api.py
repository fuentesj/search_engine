from search_engine import SearchEngine
searchEngine = SearchEngine()
from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/search_results', methods = ['POST', 'GET'])
def api_root():
	return "test"
	# Commented out for debugging purposes
	# search_term = request.args.get('search_term')
	# searchEngine.search(search_term)
	# return 'POST'

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

if __name__ == '__main__':
	app.run()