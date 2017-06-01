/**
 * Created by migs on 5/30/17.
 */


/* ************************* */
/* your javascript goes here */

// inside the function below is where you will
// do your work
// the transform function takes a string as an input
// and print out the result using the `printResult`
// function
// you can add more functions above to keep your
// code clean and readable
function transform(input) {
  if (input) {
    clearError();
    // do some transform of the user's input
    // vvvvvv HERE vvvvvv

    // your stuff HERE
    var encoded = input; //assigning a variable to input
    var alphabet = 'abcdefghijklmnopqrstuvwxyz'; //make the alphabet
    var cesar13 = 'nopqrstuvwxyzabcdefghijklm'; //make the cesar alphabet

    var decoded = []; //initializing array

    for (var i=0; i<encoded.length;i++){ //setting up the index, then saying the length of the array, then using a counter
        var enchar = encoded[i]; // This is the letter to change
        alert("this is the letter to change: " +enchar);
        var encloc = cesar13.indexOf(enchar); //This is it's position in the cesar alphabet
        alert("This is the position in cesar alphabet: " + encloc);
        var decodedChar = alphabet[encloc]; //
        alert("This is the translated letter: " + decodedChar);
        decoded.push(decodedChar);
    }
    var result = decoded.join('');
      alert("This is the result: " + result)




    // ^^^^^^ HERE ^^^^^^
    // when you've done the transform,
    // print the result
    printResult(result);
  }
  else {
    printError('Enter a value');
    focusInput();
  }
}

document.addEventListener('DOMContentLoaded', function (evt) {
  // you can rename the `transform` function
  // above, but if you do, you need to change
  // the name here, too
  setup(transform);
  focusInput();
});

/* ************************************** */
/* do not change anything below this line */

function focusInput() {
  document.querySelector('[name="input"]').focus();
}

function printResult(str) {
  document.getElementById('result').innerHTML = str;
}

function printError(str) {
  var err = document.getElementById('error');
  err.classList.add('error');
  err.innerHTML = str;
}

function clearError() {
  var err = document.getElementById('error');
  err.innerHTML = '';
  err.classList.remove('error');
}

function setup(callback) {
  document.querySelector('form')
    .addEventListener('submit', function (evt) {
    evt.preventDefault();
    var value = document.querySelector('input').value;
    callback(value);
  });
}
