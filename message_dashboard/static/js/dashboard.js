/**
 * Created by root on 3/29/15.
 */

/*
Angular js section********************
 */
(function(){

      var dashboard_app=angular.module("dashboardApp", ['ui.bootstrap'])
      .run(function($rootScope) {
          $rootScope.count_All=0
          $rootScope.count_24Hours=0;
          $rootScope.count_7Days=0;
          $rootScope.count_30Days=0;
          $rootScope.presentList=null;

      });


      var cacheAllMsg;
      var cache30days;
      var cache7days;
      var cache24hours;
      dashboard_app.factory('messagesService', function($q,$rootScope) {


         messageList = [];

         var defer=$q.defer();
         return {
            storeMessages:function(data){
               messageList=data;
               defer.resolve();
               $rootScope.$broadcast('eventFired');
            },

            getMessages:function(){
              return messageList;
            },
            getPromise:function(){
                 return defer.promise;
                //consoel.log
            }
          };

      })

      dashboard_app.factory('getAllMessagesFactory', function($http,$q,$cacheFactory){

           return {
            list: function(){

                     if(typeof cacheAllMsg !=="object" )
                          cacheAllMsg = $cacheFactory('All-Msgs');
                     var defer = $q.defer();
                     var request = $http({
                         method: "GET",
                         url: "/getmessage",
                         params: {period: 'All'},
                         headers: {'Content-Type': 'application/x-www-form-urlencoded'}


                     })
                         .success(function (response) {
                             cacheAllMsg.put("All", response);
                             defer.resolve(response)
                         })
                         .error(function (err, status) {
                             defer.reject(err);
                         });

                     return defer.promise;
                 }
            };

      });

      dashboard_app.factory('get30dayMessagesFactory', function($http,$q,$cacheFactory){
      return {
            list: function(){
                if(typeof cache30days !=="object" )
                   cache30days = $cacheFactory('30days-Msgs');
                 var defer=$q.defer();
                 var request = $http({
                        method: "GET",
                        url: "/getmessage",
                        params: {period:'30days'},
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}


                    })
                    .success(function(response){
                         cache30days.put("30days", response);
                         defer.resolve(response)
                    })
                    .error(function(err, status) {
                          defer.reject(err);
                    });
                return defer.promise;
          }
        };
      });

      dashboard_app.factory('get7daysMessagesFactory', function($http,$q,$cacheFactory){
        return {
            list: function(){
                if(typeof cache7days !=="object" )
                     cache7days = $cacheFactory('7days-Msgs');
                 var defer=$q.defer();
                 var request = $http({
                        method: "GET",
                        url: "/getmessage",
                        params: {period:'7days'},
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}


                    })
                  .success(function(response){
                         cache7days.put("7days", response);
                         defer.resolve(response)
                    })
                    .error(function(err, status) {
                          defer.reject(err);
                    });
                return defer.promise;
          }
        };
      });

      dashboard_app.factory('get24hoursMessagesFactory', function($http,$q,$cacheFactory){
        return {
            list: function(){
                if(typeof cache24hours !=="object" )
                    cache24hours = $cacheFactory('24hours-Msgs');
                 var defer=$q.defer();
                 var request = $http({
                        method: "GET",
                        url: "/getmessage",
                        params: {period:'24hours'},
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}


                    })
                   .success(function(response){
                         cache24hours.put("24hours", response);
                         defer.resolve(response)
                    })
                    .error(function(err, status) {
                          defer.reject(err);
                    });
                return defer.promise;
          }
        };
      });


      dashboard_app.factory('TypeAheadFactory', function($http) {
          return {
            get: function(callback){

                var request = $http({
                        method: "POST",
                        url: '/msg_board/search',
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                        cache:true

                    })
                     .success(callback)
                     .error(function(data, status, headers, config) {
                            //console.log(status)
                            //console.log(data)
                });

            }
          };
      });





      dashboard_app.controller("messageController",function($scope,$rootScope,$http,getAllMessagesFactory,get30dayMessagesFactory,get7daysMessagesFactory,get24hoursMessagesFactory,messagesService){




          /********Getting the message on load******************/

            getAllMessagesFactory.list().then(function(data){
               $rootScope.count_All=data.length;
               messagesService.storeMessages(data);
               //console.log(messagesService.getMessages())

            });

             get30dayMessagesFactory.list().then(function(data){
                   $rootScope.count_30Days=data.length;
                   //messagesService.storeMessages(data);
                   //console.log(messagesService.getMessages());
              });

              get7daysMessagesFactory.list().then(function(data){
                   $rootScope.count_7Days=data.length;
                   //messagesService.storeMessages(data);
                   //console.log(messagesService.getMessages());
              })

              get24hoursMessagesFactory.list().then(function(data){
                   $rootScope.count_24Hours=data.length;
                   //messagesService.storeMessages(data);
                   //console.log(messagesService.getMessages());
              })


            $rootScope.presentList='ALL';

           $scope.getMessage=function(period){


               if(period==='All')
               {
                  $rootScope.presentList='ALL';
                  if(cacheAllMsg && cacheAllMsg.get('All'))
                  {
                      var data=cacheAllMsg.get('All');
                      $rootScope.count_All = data.length;
                      messagesService.storeMessages(data);
                  }
                  else
                  {
                      getAllMessagesFactory.list().then(function (data) {
                          $rootScope.count_All = data.length;
                          messagesService.storeMessages(data);
                          //console.log(messagesService.getMessages())

                      });
                  }
               }
               else if(period==='30days')
               {

                 $rootScope.presentList='30days';
                 if(cache30days && cache30days.get('30days'))
                 {

                      var data=cache30days.get('30days');
                      console.log(data);
                      $rootScope.count_30Days = data.length;
                      messagesService.storeMessages(data);
                 }
                 else
                 {
                     get30dayMessagesFactory.list().then(function (data) {
                         $rootScope.count_30Days = data.length;
                         messagesService.storeMessages(data);
                         //console.log(messagesService.getMessages());

                     });
                 }

               }
               else if(period==='7days')
               {
                 $rootScope.presentList='7days';
                 if(cache7days && cache7days.get('7days'))
                 {
                      var data=cache7days.get('7days');
                      $rootScope.count_7Days = data.length;
                      messagesService.storeMessages(data);
                 }
                 else
                 {
                     get7daysMessagesFactory.list().then(function (data) {
                         $rootScope.count_7Days = data.length;
                         messagesService.storeMessages(data);

                         //console.log(messagesService.getMessages());
                     })
                 }
               }
               else if(period==='24hours')
               {
                 $rootScope.presentList='24hours';
                 if(cache24hours && cache24hours.get('24hours'))
                 {
                      var data=cache24hours.get('24hours');
                      $rootScope.count_24Hours = data.length;
                      messagesService.storeMessages(data);
                 }
                 else
                 {
                     get24hoursMessagesFactory.list().then(function (data) {
                         $rootScope.count_24Hours = data.length;
                         messagesService.storeMessages(data);

                         //console.log(messagesService.getMessages());
                     })
                 }
               }
           }


      })

      dashboard_app.controller("searchOptionsController",function($scope,$http,TypeAheadFactory){


            TypeAheadFactory.get(function(data){

                   $scope.messages = data;

                   //console.log($scope.messages);
             })

            $scope.dateValidation=function(){

                if($scope.values==undefined || $scope.values.startDate==='' || $scope.values.endDate==='' )
                {
                    return false;
                }
                var startDate = new Date($scope.values.startDate);
                var endDate = new Date($scope.values.endDate);

                /*
                 To check if start date is greater than end date
                 */

                if(startDate.getTime()>endDate.getTime()){
                    return true;
                }
                else{
                    return false;
                }
            };



            $scope.sendData=function(){

                if(!$scope.searchForm.$error.email && !$scope.isInValid)  {

                       /****Check if the form is empty******/
                        if($scope.values===undefined ||

                            (
                                ($scope.values.email===undefined ||$scope.values.email==='') &&
                                ($scope.values.company===undefined || $scope.values.company==='') &&
                                ($scope.values.person===undefined || $scope.values.person==='') &&
                                ($scope.values.keyword===undefined || $scope.values.keyword==='') &&
                                ($scope.values.startDate===undefined || $scope.values.startDate==='') &&
                                ($scope.values.end_date===undefined || $scope.values.end_date==='')
                            )
                          )
                            {
                                $scope.isEmpty=true;
                                return true;
                            }

                        var request = $http({
                        method: "GET",
                        url: "/msg_board/searchmessage",
                        params: {
                                     email:$scope.values.email,
                                     organization:$scope.values.company,
                                     person:$scope.values.person,
                                     keyword:$scope.values.keyword,
                                     start_date:$scope.values.startDate,
                                     end_date:$scope.values.endDate
                                 },
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}

                    }).
                        success(function(data, status, headers, config) {
                                //console.log(data)
                        }).
                        error(function(data, status, headers, config) {
                                        // called asynchronously if an error occurs
                        // or server returns response with an error status.


                     });

                    return false;
                }

            }

            $scope.resetSearchForm = function() {

                  $scope.values.email = '';
                  $scope.values.company = '';
                  $scope.values.person = '';
                  $scope.values.keyword = '';
                  $scope.values.startDate = '';
                  $scope.values.endDate = '';
                  $scope.searchForm.$setPristine(true);

          };


          $scope.closeAlert = function() {

              return false;
          };

      })

dashboard_app.controller("messagesBlockCtrl",function($rootScope,$scope,$http,getAllMessagesFactory,get30dayMessagesFactory,get7daysMessagesFactory,get24hoursMessagesFactory,messagesService){




       $scope.$on('eventFired', function(event, data) {

            var promise=messagesService.getPromise()
                promise.then(function(){
                $scope.message_list=messagesService.getMessages();
            })

      });

      $scope.deleteMsg=function(id){

           var request = $http({
                method: "GET",
                url: "/msg_board/deletemessage",
                params: { id:id  },
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}

                }).
                success(function(data, status, headers, config) {
                        if(status==200) {
                         cacheAllMsg.removeAll();
                         cache30days.removeAll();
                         cache7days.removeAll();
                         cache24hours.removeAll();
                         //console.log($rootScope.presentList)

                          var promise_1=getAllMessagesFactory.list().then(function (data) {
                            $rootScope.count_All = data.length;
                         });

                          var promise_2=get30dayMessagesFactory.list().then(function (data) {
                         $rootScope.count_30Days = data.length;
                         });

                          var promise_3=get7daysMessagesFactory.list().then(function (data) {
                         $rootScope.count_7Days = data.length;
                         });

                         var promise_4=get24hoursMessagesFactory.list().then(function (data) {
                         $rootScope.count_24Hours = data.length;
                         });


                         if($rootScope.presentList==='ALL')
                         {
                             promise_1.then(function(){
                               var data=cacheAllMsg.get('All');
                               messagesService.storeMessages(data);
                             })


                         }
                         else if($rootScope.presentList==='30days')
                         {
                             promise_2.then(function(){
                                  var data=cache30days.get('30days');
                                  messagesService.storeMessages(data);
                             })


                         }
                         else if($rootScope.presentList==='7days')
                         {
                             promise_3.then(function(){
                                 var data=cache7days.get('7days');
                                 messagesService.storeMessages(data);
                             });


                         }
                         else if($rootScope.presentList==='24days')
                         {
                                promise_4.then(function(){
                                    var data=cache24hours.get('24hours');
                                    messagesService.storeMessages(data);
                                });


                         }

                        }


                }).
                error(function(data, status, headers, config) {
                                // called asynchronously if an error occurs
                // or server returns response with an error status.
           });
      }



});


})();

/*
Jquery section******************
 */

$( document ).ready(function() {

    $('.logout-btn').click(function () {
        $.ajax({
             url: "/msg_board/logout",
             type:'POST',
             header: {
                 isValid: True
             }
         })
             .done(function (data, status, d) {

                alert(data);

             })
             .fail(function () {

             })

       });

    /*********Initialize date-picker************************/
      $('#datePicker1')
        .datepicker({
            format: 'mm/dd/yyyy'
        });

       $('#datePicker2')
        .datepicker({
            format: 'mm/dd/yyyy'
        });

     /***********************************Typeahead for organization*************/

    /**$('#org').typeahead({

            hint: true,
            highlight: true,
            minLength: 1
        },
        {
            name:'organizations',
            displayKey:'value',
            source: function(query,process){

                $.ajax({
                    url:'/search/org',
                    type:'POST',
                    data:'search_term='+query,
                    dataType:'JSON',
                    success:function(data){
                        var orgs=[];
                        $.each(data, function(idx, obj) {
                            //console.log(obj.fields.sender_organization);
                            orgs.push({
                                value:obj.fields.sender_organization
                            });
                        });

                        process(orgs);

                    }

            });
        }

    });**/

     /***********************************Typeahead for email*************/
   /* $('#email_id').typeahead({

            hint: true,
            highlight: true,
            minLength: 1
        },
        {
            name:'emails',
            displayKey:'value',
            source: function(query,process){

                $.ajax({
                    url:'/search/email',
                    type:'POST',
                    data:'search_term='+query,
                    dataType:'JSON',
                    success:function(data){
                        var emails=[];
                        $.each(data, function(idx, obj) {
                            //console.log(obj.fields.sender_organization);
                            emails.push({
                                value:obj.fields.sender_email
                            });
                        });

                        process(emails);

                    }

            });
        }

    });*/

      /***********************************Typeahead for name*************/
   /**  $('#name_id').typeahead({

            hint: true,
            highlight: true,
            minLength: 1
        },
        {
            name:'names',
            displayKey:'value',
            source: function(query,process){

                $.ajax({
                    url:'/search/name',
                    type:'POST',
                    data:'search_term='+query,
                    dataType:'JSON',
                    success:function(data){
                        var names=[];
                        $.each(data, function(idx, obj) {
                            console.log(obj.fields.sender_organization);
                            names.push({
                                value:obj.fields.sender_name
                            });
                        });

                        process(names);

                    }

            });
        }

    });**/

});


