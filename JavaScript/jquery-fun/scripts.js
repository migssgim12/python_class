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

$( function() {
    // run the currently selected effect
    function runEffect() {
      // get effect type from
      var selectedEffect = $( "#effectTypes" ).val();

      // Most effect types need no options passed by default
      var options = {};
      // some effects have required parameters
      if ( selectedEffect === "scale" ) {
        options = { percent: 50 };
      } else if ( selectedEffect === "size" ) {
        options = { to: { width: 200, height: 60 } };
      }

      // Run the effect
      $( "#effect" ).toggle( selectedEffect, options, 500 );
    };

    // Set effect from select menu value
    $( "#button" ).on( "click", function() {
      runEffect();
    });
  } );
