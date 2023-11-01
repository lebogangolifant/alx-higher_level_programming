// Toggles the class of the <header> element when the user clicks on the tag

/* global $ */
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
