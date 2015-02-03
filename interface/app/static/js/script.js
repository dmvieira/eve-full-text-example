// Default file for javascript code in search interface

$(function() {

    $("#search-input").autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "http://localhost:5000/hotel/?projection={'city':1}",
                dataType: "jsonp",
                data: {
                    q: request.term
                },
                success: function( data ) {
                    response( data );
                }
            });
        },
        minLength: 3,
        select: function( event, ui ) {
            //log( ui.item ?
            //    "Selected: " + ui.item.label :
            //    "Nothing selected, input was " + this.value);
        },
        open: function() {
            $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
        },
        close: function() {
            $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
        }
    });
});