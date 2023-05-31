const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data) {
  const results = data.results;
  results.forEach(function (result) {
    $('ul#list_movies').append('<li>' + result.title + '</li>');
  });
});
