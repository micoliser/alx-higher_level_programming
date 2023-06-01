window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const ln = 'https://fourtonfish.com/hellosalut/?lang=';
    $.get(ln + lang, function (data, statusCode) {
      $('DIV#hello').text(data.hello);
    });
  });
};
