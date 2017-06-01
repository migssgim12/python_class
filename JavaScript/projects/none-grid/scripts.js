
"use strict"

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
      } else if ( selectedEffect === "transfer" ) {
        options = { to: "#button", className: "ui-effects-transfer" };
      } else if ( selectedEffect === "size" ) {
        options = { to: { width: 200, height: 60 } };
      }

      // Run the effect
      $( "#effect" ).effect( selectedEffect, options, 500, callback );
    };

    // Callback function to bring a hidden box back
    function callback() {
      setTimeout(function() {
        $( "#effect" ).removeAttr( "style" ).hide().fadeIn();
      }, 1000 );
    };

    // Set effect from select menu value
    $( "#button" ).on( "click", function() {
      runEffect();
      return false;
    });
  } );

function rgb() {
  var $red = Math.floor((Math.random() * 255) + 1);
  var $green = Math.floor((Math.random() * 255) + 1);
  var $blue = Math.floor((Math.random() * 255) + 1);
  return {'red': $red, 'green': $green, 'blue': $blue}
}
$( function() {
    $( "#dialog" ).dialog();
  } );

$('.box1').hover(function(event){
  // creating the mouseover event
      var hue = rgb();
      //  assigning three variables to random color method
      var hoverText = $(this).text();
      $('#none').text(hoverText);

       $(this).css('background-color', `rgb(${hue.red}, ${hue.green}, ${hue.blue}`).css('transition', '0.25s', 'ease-in');
            // this allows the colors to tranform

},  function(){
      $('#none').text(' NONE ');
});
