app.factory("searchEngineService", ["$http", function($http) {

	return {
		getSearchResults: function() {
			return $http({
					method: 'GET',
					url: 'http://localhost:5000/search_results'
				}).then(function successCallback(response) {
					return response
				}, function errorCallback(err) {
					return err;
				});
			}
		}
}]);
	


