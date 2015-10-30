app.controller("SearchEngineController", function($scope, searchEngineService) {

	$scope.searchTerm = ""
	$scope.searchResults = "";
	
	$scope.getSearchResults = function() {
		searchEngineService.getSearchResults(this.searchTerm).then(function(result) {
			console.log(result)
			$scope.searchResults = result.data;
		});
	};
});