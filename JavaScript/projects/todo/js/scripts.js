

"use strict"

function incrementCounter() {
  // increments the counter by 1
  var $counter= $("#counter").text();
  var intify = Number($counter);
  var counted = String(intify+1);
  $('#counter').html(counted);
}


function addToList(item) {
  var $listItem = $('<li class="myclass">').text(item);
  $listItem.on('click', function(event){
    // event handler for clicking on list items
    $(this).css('text-decoration', 'line-through');
    incrementCounter();
  });
  $('#list').append($listItem);
}


$('#sub_button').on('click', function(event){
  // event handler for handling todo item
  event.preventDefault();
  var output = $('#todo').val();

  addToList(output);
  $('#todo').val('');
});
