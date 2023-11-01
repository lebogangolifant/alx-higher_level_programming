// Fetches and prints how to say “Hello” depending on the language

/* global $ */
$(document).ready(function () {
  // Attach click event handler to the Translate button
  $('#btn_translate').click(translateHello);

  // Function to fetch and display the translation
  function translateHello () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    // Send a GET request using the Fetch API
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        if (data.code && data.code === 'none') {
          $('#hello').text('Language code not found');
        } else {
          $('#hello').text(data.hello);
        }
      })
      .catch(error => {
        $('#hello').text('Error: Language code not found');
        console.error(error);
      });
  }
});
