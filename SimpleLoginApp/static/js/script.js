var app = angular.module('myapp', ['ngRoute']);
app.config(function($routeProvider) {
	console.log("in route provider");
	$routeProvider
	.when("/", {
		templateUrl : "templates/index.html",
		controller : "login_controller"
	}).when("/signIn", {
		templateUrl : "templates/signup.html",

	});
});

app.controller("login_controller",function($scope,$http){
	console.log("Reporting from login controller");
	console.log("Username-- "+$scope.username);
	console.log("Password-- "+$scope.password);

	$scope.show=function(){
	console.log("Hello");
	console.log("Username== "+$scope.username);
	console.log("Password== "+$scope.password);
	$http({
			method:'POST',
			url:'/signIn',
			data:{
				"username":$scope.username,
				"password":$scope.password
			}
		})
	}
});
