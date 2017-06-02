//very important pattern
var data;
$.ajax({
    url: 'https://api.randomuser.me',
    method: 'GET',
    data: {'results':5},
    success: function(rsp){
      console.log(rsp);
      data = rsp;
    },
    error: function(err){
      console.log(err);
  }
});
