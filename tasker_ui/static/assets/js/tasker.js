$(document).ready(function() {
   $('.tasker-login').on('click', (e) => {
       e.preventDefault();
       console.log("Clicked");
       $('#login-form').modal('show');
   });
});