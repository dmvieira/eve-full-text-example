// Default file for javascript code in search interface

function gen_new_suggestion(text){
    // Generate html for autocomplete suggestions
    code = "<li class='suggest'>"+text+"</li>";
    return code;
}

function gen_new_result(object){
    // Generate html for autocomplete suggestions
    code = "<div class='col-xs-12'>" +
           "<hr>" +
           "<h4>"+object.name+"</h4>" +
           "<p>"+object.location+"</p>" +
           "<small>"+object.phone+"</small>" +
           "</div>";
    return code;
}

$(function() {

    // Monitoring search-input for each keyup
    // It's a simple autocomplete made because I had errors with mongodb _id
    $("#search-input").keyup(function(){
        $.ajax({

            url: city_url + '?name='+$(this).val()

        })
            .done(function( data ) {
                var objects = JSON.parse(data);
                $('#search-suggestions').html('');
                for (i = 0; i < objects.length; i++){
                    // add suggestions to html
                    $('#search-suggestions').html($('#search-suggestions').html()+gen_new_suggestion(objects[i]._id));
                }
                $('#search-suggestions').html($('#search-suggestions').html()+'</ul>');
            });
    });

    // Monitoring each suggestion for click event.
    // When clicked, suggestion goes to input and force html clean
    $("#search-suggestions").on('click', '.suggest', function(){
        $("#search-input").val($(this).html());
        $("#search-suggestions").html('');
    })

    // Intercepts submit call and load hotels by ajax
    $("#search-form form").submit(function(event) {
        event.preventDefault();

        $.ajax({

    url: hotel_url + '?city_name='+$("#search-input").val()

    })
  .done(function( data ) {
      var objects = JSON.parse(data);
      $('#search-results').html('<h1>Results for '+$("#search-input").val()+'</h1>');
      for (i = 0; i < objects.length; i++){
          $('#search-results').html($('#search-results').html()+gen_new_result(objects[i]));
      }
    })

    });
});