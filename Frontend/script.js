$(document).ready(function(){
  $("#create_user").click(function(){
     var username = $('#username').val();
     var password = $('#password').val();
     var email = $('#email').val();
     var url = 'http://0.0.0.0:5000/create_user';
     var data = { 'username' : username, 'email': email, 'password': password}
     $.post(url,
     		data,
     		function(data,status){
     			console.log(data)
     			$("#Response_user").text(data);
     		});
  });
  $("#login_user").click(function(){
     var username = $('#username').val();
     var password = $('#password').val();
     var url = 'http://0.0.0.0:5000/login';
     var data = { 'username' : username, 'password': password}
     $.post(url,
     		data,
     		function(data,status){
     			console.log(data)
     			$("#Response_login").text(data);
     		});
  });
});