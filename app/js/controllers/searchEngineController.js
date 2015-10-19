app.controller("SearchEngineController", function($scope, searchEngineService) {

	$scope.searchResults = "foobar";
	
	$scope.getSearchResults = function() {
		$scope.searchResults = searchEngineService.getSearchResults();
	};

});