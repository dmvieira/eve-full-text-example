// Default file for javascript code in search interface

$(function() {

    $("#search-input").magicSuggest({
        data: city_url,
        valueField: '_id',
        displayField: '_id',
        mode: 'remote',
        method: 'get',
        queryParam: 'name'
    });
});