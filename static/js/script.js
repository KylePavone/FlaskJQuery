$(document).ready(function(){

$(".addform").click(function(){
    var elem = $(".form-contact").clone()
    $("form").removeClass("form-contact")
    $(this).after(elem)
    });

})