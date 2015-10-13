app.controller("SearchEngineController", ["$scope", "searchEngineService", function($scope, searchEngineService) {

	$scope.searchResults = {};


	$scope.sendSearchQuery = function() {
		searchEngineService.success(function(data) {
				$scope.searchResults = data;
			})
	};


}]);