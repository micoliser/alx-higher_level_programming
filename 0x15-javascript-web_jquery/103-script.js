window.onload = function () {
  $('INPUT#btn_translate').click(function () {
   salut();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      salut();
    }
  });
};

function salut () {
  const lang = $('INPUT#language_code').val();
  const ln = 'https://fourtonfish.com/hellosalut/?lang=';
  $.get(ln + lang, function (data, statusCode) {
    $('DIV#hello').text(data.hello);
  });
}
