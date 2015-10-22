app.controller("SearchEngineController", function($scope, searchEngineService) {

	$scope.searchResults = "";
	
	$scope.getSearchResults = function() {
		searchEngineService.getSearchResults().then(function(result) {
			console.log(result)
			$scope.searchResults = result.data;
		});
	};
});