from search_engine import SearchEngine
searchEngine = SearchEngine()
from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/search_results', methods = ['POST'])
def api_root():
	search_term = request.args.get('search_term')
	searchEngine.search(search_term)
	return 'POST'


if __name__ == '__main__':
	app.run()