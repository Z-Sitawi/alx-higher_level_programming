document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const lang = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response not ok');
        }
        return response.json();
      })
      .then(data => {
        $('#hello').text(data.hello);
      })
      .catch(error => {
        console.log('Error fetching data:', error);
      });
  }
});
