// Default file for javascript code in search interface

$(function() {

    $("#search-input").autocomplete({
        serviceUrl: city_url,
        paramName: 'name',
        transformResult: function(response) {
            return {
                suggestions: $.map(response.myData, function(dataItem) {
                    return { value: dataItem['_id'], data: dataItem['_id'] };
                })
            };
        }

    });
});