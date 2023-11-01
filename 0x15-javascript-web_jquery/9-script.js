// fetch the translation of "hello" from a URL and display it in the HTML tag

/* global $ */
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('#hello').text(data.hello);
});
