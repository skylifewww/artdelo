var topPos; 
$(document).ready(function(){
topPos = $("#menu").offset().top; 
});
$(document ).scroll(function(){
if(topPos < $(document).scrollTop())
$("#menu").addClass("fixed");
else 
$("#menu").removeClass("fixed");
});