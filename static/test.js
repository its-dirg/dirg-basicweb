    var app = angular.module('main', ['toaster']);

    app.factory('testFactory', function ($http) {
        return {
            getTests: function (treeType) {
                //Makes an rest request to the server part (testHandler).
                //This request contains parameters
                return $http.get("/list", {params: { "parameter": treeType}});
            }
        };
    });

    //Controller which will be executed when the web page is loaded
    app.controller('IndexCtrl', function ($scope, testFactory, toaster) {

        //Variables which will be accessible in index.mako
        $scope.list = [{'id': 'Basic element1'}, {'id': 'Basic element2 (hidden)', 'visible': false}, {'id': 'Basic element3'}];
        $scope.parameter = "testParameter";

        //Normal javascript variables which won't be accessible in index.mako
        var elementIndex = 0;


        // Will be executed when the "Add item to list" button is pressent in index.mako
        $scope.addElement = function (newElement) {
            elementIndex++;
            $scope.list.push({'id': newElement + elementIndex});
        };

        //The method which is called when "testFactory.getTests" has returned successfully
        var getListSuccessCallback = function (data, status, headers, config) {
            //Enter the values returned by the server
            for (var i = 0; i < data.length; i++){
                $scope.list.push(data[i]);
            }

            //A notification library named Toaster formats and print success
            toaster.pop('success', "Notification", "successfully made a Rest request");
        };

        //The method which is called when "testFactory.getTests" has returned an error
        var errorCallback = function (data, status, headers, config) {
            //A notification library named Toaster formats and print error
            toaster.pop('error', "Notification", "error");
        };

        // Will be executed when the "Get Elements From Server" button is pressent in index.mako
        $scope.getElementsFromServer = function () {
            //Executing getTests in the test factory
            testFactory.getTests($scope.parameter).success(getListSuccessCallback).error(errorCallback);
        };
    });

