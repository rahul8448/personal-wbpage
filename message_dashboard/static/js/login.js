/**
 * Created by root on 3/3/15.
 */

(function(){

     var login_app=angular.module("loginApp", []);

     login_app.controller("formController",function($scope,$http){

         $scope.user = {};
         $scope.user.email = '';
         $scope.user.password='';

     })

})();

    //test@gmail.com

//Test2014$$

// $http.post('/msg_board/authenticate',{user_name:$scope.user.email,pass_word:$scope.user.password}).
