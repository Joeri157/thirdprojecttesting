 $(document).ready(function(){
    $('.sidenav').sidenav({edge: "down"});
    $(".dropdown-trigger").dropdown({ coverTrigger: false});
    $('.slider').slider({ indicators: false});
    $('input#input_text, textarea#upload_description').characterCounter();
  });