// Default file for javascript code in search interface

function gen_new_suggestion(text){
    code = "<li class='suggest'>"+text+"</li>";
    return code;
}

$(function() {
    $("#search-input").keyup(function(){
        $.ajax({

            url: city_url + '?name='+$(this).val()

        })
            .done(function( data ) {
                var objects = JSON.parse(data);
                $('#search-suggestions').html('');
                for (i = 0; i < objects.length; i++){
                    $('#search-suggestions').html($('#search-suggestions').html()+gen_new_suggestion(objects[i]._id));
                }
                $('#search-suggestions').html($('#search-suggestions').html()+'</ul>');
            });
    });
    $("#search-suggestions").on('click', '.suggest', function(){
        $("#search-input").val($(this).html());
        $("#search-suggestions").html('');
    })

    $("#search-form form").submit(function(event) {
        event.preventDefault();

        $.ajax({

    url: hotel_url + '?city_name='+$("#search-input").val()

    })
  .done(function( data ) {
      var objects = JSON.parse(data);
      $('#search-suggestions').html('');
      for (i = 0; i < objects.length; i++){
          console.log(objects[i]);
      }
    })

    });
});