"use strict"

function addBox(title, firstName, lastName, dob, email, picture) {
  var $addBox = $('<div>', {'class': 'user'});
  var $image = $('<img>').attr('src', picture);
  $addBox.append(`Name: ${title} ${firstName} ${lastName}

  Date of Birth: ${dob}  Email ${email}`);

  $addBox.on('click', function(event){
  });
  console.log(`Name: ${firstName}`);
  $('#userbox').append($image, $addBox);
};

function sifter(data){
  $.each(data.results, function(index, user) {
    let title = user.name.title;
    let firstName = user.name.first;
    let lastName = user.name.last;
    let dob = user.dob;
    let email = user.email;
    let picture = user.picture.thumbnail;
    addBox(title, firstName, lastName, dob, email, picture);
  });

}


function fetcher(){
  var data;
  $.ajax({
      url: 'https://api.randomuser.me',
      method: 'GET',
      data: {'results':5},
      success: function(rsp){
        console.log(rsp);
        data = rsp;
        sifter(data);
      },
      error: function(err){
        console.log(err);
    }
  });
}


$('#generate').on('click', function(event){
  // event handler for handling todo item
  event.preventDefault();
  // alert('hi');
  fetcher();
});
