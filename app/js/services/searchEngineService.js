app.factory("searchEngineService", ["$http", function($http) {

	return $http.get("http://localhost/search_results")
				.succcess(function(data) {
					return data;
				})
				.error(function(err) {
					return err;
				});
}]);
	


