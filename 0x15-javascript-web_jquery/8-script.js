$(document).ready(function () {
        $.ajax({
                url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
                method: 'GET',
                success: function (data) {
                        for (const item in data.results) {
                                $('#list_movies').append('<li>' + data.results[item].title + '</li>');
                        }
                }
        })
});