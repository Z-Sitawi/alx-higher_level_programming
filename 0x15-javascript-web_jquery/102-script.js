#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function (){
    const lang = $('#language_code').val();
    let url = 'https://hellosalut.stefanbohacek.dev/?lang='+lang;
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
  })
});