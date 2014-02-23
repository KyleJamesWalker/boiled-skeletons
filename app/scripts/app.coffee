HomeController = require 'controllers/home'
ViewOneController = require 'controllers/view1'
ViewTwoController = require 'controllers/view2'

app = angular.module('YourSkeletonsApplication',
    [
        'ui.router'
    ]
)

app.config ($stateProvider, $urlRouterProvider) ->
    $urlRouterProvider
        .when('/v1', '/view1')
        .when('/v2', '/view2')
        .otherwise('/')

    $stateProvider
        .state 'home',
            controller: HomeController
            url: '/'
            templateUrl: 'partials/home.html'

        .state 'view1',
            controller: ViewOneController
            url: '/view1'
            templateUrl: 'partials/view1.html'

        .state 'view2',
            controller: ViewTwoController
            url: '/view2'
            templateUrl: 'partials/view2.html'

        .state 'about',
            url: '/about'
            templateUrl: 'partials/about.html'

        .state 'contact',
            url: '/contact'
            templateUrl: 'partials/contact.html'
