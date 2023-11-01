// Fetches and prints how to say “Hello” depending on the language

/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    $.ajax({
      url: apiUrl,
      type: 'GET',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      },
      error: function () {
        $('DIV#hello').text('Error: Language code not found');
      }
    });
  });
});
