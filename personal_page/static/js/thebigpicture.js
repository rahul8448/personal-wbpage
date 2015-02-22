/*
 This js file has all the custom functions necessary for the application
*/


$(document).ready(function() {

    //Function to validate the message form in the home page
    //USes the jquery validation library : Source :http://jqueryvalidation.org/

      /*Read JSON*/
    var getData=function () {
         var jsonSkillData;
         var storeSkillData=function(data)
         {
            jsonSkillData=data;
         }
         $.ajax({
          url: "/static/data/skill.json",
          dataType: "json",
          async: false,
          success: function (data) {
                storeSkillData(data);
          }

      });
       var returnSkillData=function(){
             return jsonSkillData;
       }
        return returnSkillData;
    }

    $('form').validate({
        rules: {
            full_name: {
                maxlength: 50,
                required: true
            },
            phone_num: {
                phoneUS: true
            },
            email: {
                required: true,
                email: true
            },
            subject: {
                minlength: 9,
                maxlength: 40,
                required: true
            },
            company: {
                maxlength: 50
            },
            content: {
                maxlength: 200
            }

        },
        messages: {
            full_name: {
                required: "Name field cannot be empty"

            },
            phone_num: {
                phoneUS: "Number should be a valid US number"

            },
            subject: {
                required: "Message subject cannot be empty"
            }

        },

        submitHandler: function(form) {
            submitData();
        },

        highlight: function(element) {
            $(element).closest('.input-group').addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).closest('.input-group').removeClass('has-error');
        },
        errorClass: 'help-block',
        errorPlacement: function(error, element) {
            console.log(element);
            error.insertAfter(element.parent());

        }

    });

    //Post data from message to database
    var submitData = function() {
        //Sending json data
        $.ajax({
                url: "/msg/send",
                type: 'POST',
                data: {

                    full_name: $('#nameField').val(),
                    phone_num: $('#contact').val(),
                    email: $('#emailField').val(),
                    company: $('#companyField').val(),
                    subject: $('#subjectField').val(),
                    message: $('#messageField').val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                beforeSend: function() {
                    if ($(".alert").length) {
                        $(".alert").remove();
                    }
                }
            }).done(function(data, status, d) {

                if (status == 'success') {
                    $('#nameField').val('');
                    $('#contact').val('');
                    $('#emailField').val('');
                    $('#companyField').val('');
                    $('#subjectField').val('');
                    $('#messageField').val('');
                    $('<div class="alert alert-success alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Well done!</strong> Your message has been successfully sent.</strong></div>').appendTo('.form-group');
                    $('.alert').css({
                        "width": "50%",
                        "margin-top": "1%"
                    });

                }

            })
            .fail(function() {

                $('<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Ooops..!</strong> Your message could not be sent at this moment.Try again later</strong></div>').appendTo('.form-group');
                $('.alert').css({
                    "width": "50%",
                    "margin-top": "1%"
                });

            })

    }

    //Ajax request for downloading resume from server
    /*var download_resume=function(){
        $.ajax({
                url: "/static/data/Rahul_Sharma_Resume.pdf",
                type: 'GET'
               }).done(function(data, status, d) {

                if (status == 'success') {



                }

            })
            .fail(function() {


            })
    }*/

    $(".navbar-nav").children().click(function(e) {


        $(".navbar-nav").children().removeClass("active")
        $(this).addClass("active")
    });


    $(".close").click(function() {

        $(".navbar-nav").children().removeClass("active")
        $(".navbar-nav li:nth-child(1 )").addClass("active")
        $(".navbar-nav li:nth-child(1 )").children().focus();

    });


    /*For Cerner*/
    $('.more-info-cerner').popover({
        html: true,
        placement: 'right',
        title: 'Details',
        delay: {
            "show": 5,
            "hide": 5
        },
        trigger: 'hover',
        content: function() {
            return $('#content_Cerner').html();
        }
    });



    /*For UNL*/
    $('.more-info-unl').popover({
        html: true,
        placement: 'right',
        title: 'Details',
        trigger: 'hover',
        delay: {
            "show": 5,
            "hide": 5
        },
        content: function() {
            return $('#content_unl').html();
        }
    });

    /*For Accenture*/
    $('.more-info-acc').popover({
        html: true,
        placement: 'right',
        title: 'Details',
        trigger: 'hover',
        delay: {
            "show": 5,
            "hide": 5
        },
        content: function() {
            return $('#content_acc').html();
        }
    });


    $(function() {
        $('[data-toggle="tooltip"]').tooltip()
    })

     /*Load data*/
     var skillData=getData();

    /*Loading selection category*/
    $.each(skillData(),function(key,value){
        var category=value["category"];
        $( ".dropdown-menu" ).append( "<li role='presentation'><a role='menuitem' tabindex='-1' href='#'>"+category+"</a></li>" );
    });

    /*Default checkbox selection:Tabular*/
    $("#tabular").prop("checked", true);

     $.each( skillData(), function( key, val ) {
          if(val["category"]==="Languages")
          {
             var contents=val["content"];
             $.each( contents, function( key, value ){

                   var name=value["name"];
                   var exp=value["experience"]
                   var color=value["color"]
                   $( ".skill_table tbody" ).append( "<tr><td>"+name+"</td><td>"+exp+"</td></tr>" );

              });
           }
      });


     $(".dropdown-menu li").click(function(){
               var selected_category=$(this).children().text();
               $( ".category h3 span" ).replaceWith( " <span id='current_category'>"+selected_category+"</span>" );
                 $( ".skill_table tbody tr" ).remove();
                 $.each( skillData(), function( key, val ) {
                      if(val["category"]===selected_category )
                      {
                         var contents=val["content"];
                         $.each( contents, function( key, value ){

                               var name=value["name"];
                               var exp=value["experience"]
                               var color=value["color"]
                               $( ".skill_table tbody" ).append( "<tr><td>"+name+"</td><td>"+exp+"</td></tr>" );

                          });

                          if($('input[name=display]:checked').val()=="piechart")
                          {
                                generatePieChart(selected_category);
                          }
                          if($('input[name=display]:checked').val()=="barchart")
                          {
                              $(".bar-chart").empty();
                              generateBarGraph(selected_category);

                          }
                       }


                  });
      });



      $('input:radio[name="display"]').change(
       function(){
           if ($(this).val() === 'barchart') {
              $(".tabular").hide();
              $(".pie-chart").empty();
              generateBarGraph($('#current_category').text());

           }
           /*else if(($(this).val() == 'piechart')) {//Future
              $(".tabular").hide();
              $(".bar-chart").remove();
              generatePieChart($('#current_category').text());
           }*/
           else{
                $(".chart").empty();
                $(".pie-chart").empty();
                $(".tabular").show();

           }
      });


      var generateBarGraph=function(current_category){


           $(".chart").empty();
           $('.chart').append('<h3>Current Category: <span id="current_category">'+current_category+'</span></h3>')
           var max_width=$('.category').width();

           $.each( skillData(), function( key, val ) {
               if(val["category"]===current_category ){
               var data=val["content"];
               var size=data.length;
               var barHeight = 25;
               var height=barHeight*size+90;


               var svgContainer = d3.select(".chart").append("svg")
                             .attr("width", max_width)
                             .attr("height", function(d){return height+"";})
                             .attr("class","bar-chart")
                           .append("g");


               $('.bar-chart').css("margin-top","8%");

               var axisScale=d3.scale.ordinal()
                   .domain(["Novice","Advanced-Beginner","Competent","Advanced-Competent","Proficient","Expert"])
                   .rangeBands([0,max_width]);

               var xAxis = d3.svg.axis()
                        .scale(axisScale)
                        .orient("bottom")
                        .ticks(7)
                        .tickValues(["Novice","Advanced-Beginner","Competent","Advanced-Competent","Proficient","Expert"]);


              var ycor=(barHeight*size)+10;

              var xAxisGroup = svgContainer.append("g")
                               .attr("class", "x-axis")
                               .attr("transform", function(d){ return "translate(0," + ycor + ")"})
                               .call(xAxis)
                               .selectAll("text")
                                .attr("transform","translate(0,30) rotate(30)")


               var g=svgContainer.selectAll(".bar-g")
                  .data(data)
                 .enter().append("g")
                 .attr("class","bar-g");

                var bar=g.append("rect")
                  .attr("class", "bar")
                  .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; })
                  .attr("height", barHeight - 1)
                  .attr('width', 0);

               bar.transition()
                  .delay(200)
                  .duration(700)
                  .ease("linear")
                  .attr("width", function(d) {return axisScale(d.exp_words);})
                  .attr("fill", function(d) { return d.color; });

               g.append("text")
                  .attr("x", function(d) {  return axisScale(d.exp_words)*0.1 ;})
                  .attr("y", function(d, i) {return  (barHeight)*i+10;} )
                  .attr("dy", ".25em")
                  .attr("class", "bar-text")
                  .text(function(d) {
                   var name=d.name;
                   if(name==="Test Driven Development")
                   {
                     name="TDD";
                   }
                   if (name==="Continuous Integration")
                   {
                     name="CI";
                   }
                    return name;
                   })
                   .transition()
                   .delay(300)
                   .duration(300);

               }

           });

      }

      /*
      Download resume on download button click
      */

      $('.download_btn').click(function(event){

            event.preventDefault();
            window.open($(this).attr("href"), "popupWindow", "width=600,height=600,scrollbars=yes");

      });
      //For future
     /* var generatePieChart=function(current_category){

           $.each( skillData(), function( key, val ) {

               if(val["category"]===current_category ){

                     console.log(val["content"])
               }

           });

      }*/
 });












