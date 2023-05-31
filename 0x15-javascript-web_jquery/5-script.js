function addItem () {
  $('ul.my_list').append('<li>Item</li>');
}

$('div#add_item').click(addItem);
