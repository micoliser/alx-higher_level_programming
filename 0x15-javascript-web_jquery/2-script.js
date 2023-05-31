function changeColor () {
  $('header').css('color', '#FF0000');
}

$('div#red_header').on('click', changeColor);
