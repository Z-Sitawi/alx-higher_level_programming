#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  const myList = $('.my_list');
  const _add = $('#add_item');
  const _remove = $('#remove_item');
  const _clear = $('#clear_list');

  _add.click(function () {
    myList.append('<li>Item</li>');
  });

  _remove.click(function () {
    myList.children('li').last().remove();
  });

  _clear.click(function () {
    myList.children('li').remove();
  });
});
