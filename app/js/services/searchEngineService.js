app.factory("searchEngineService", ["$http", function($http) {

	return {
		getSearchResults: function(search_term) {
			return $http({
						method: 'GET',
						url: 'http://localhost:9200/_search?q=tag:'+search_term
					}).then(
						function successCallback(response) {
							console.log("inside successCallback!")
							return response;
						},
						function errorCallback(err) {
							return err;
						}
					);
				}
			}
}]);
	


