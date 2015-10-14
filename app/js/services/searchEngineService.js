app.factory("searchEngineService", ["$http", function($http) {

	return $http({
		method: 'GET',
		url: 'http://localhost:5000/search_results'
	}).then(function successCallback(response) {


	}, function errorCallback(response) {


	});
}]);
	


