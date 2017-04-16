var app = angular.module('myapp', ['ngRoute']);
app.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/ds', {
                 templateUrl: '/static/partials/ds.html',
                 controller:"ds_controller"
             }).
             when('/wca', {
                 templateUrl: '../static/partials/wca.html',
                 controller:"wca_controller"
             }).when('/ss', {
                 templateUrl: '../static/partials/ss.html',
                 controller:"ss_controller"
             }).when('/admin', {
                 templateUrl: '../static/partials/admin.html',
                 controller:"admin_controller"
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);

app.controller("ds_controller",function($scope,$http){
	console.log("Reporting from ds controller");
	});

app.controller("wca_controller",function($scope,$http){
	console.log("Reporting from wca controller");
	});



