$(document).ready(function(){
    $(".dropdown-trigger").dropdown({coverTrigger: false});
    $('.slider').slider({indicators: false});
    $('input#input_text, textarea#upload_description, textarea#comment_description').characterCounter();
    $('.collapsible').collapsible();


    $(".dropdown-trigger1").dropdown({
        coverTrigger: false,
        alignment: "right"
        });
    $('.modal').modal();

// Load more function
    $(".card").slice(0, 2).show();
    $(".loadmore").on('click', function (e) {
        e.preventDefault();
        $(".card:hidden").slice(0, 2).slideDown();
        if ($(".card:hidden").length == 0) {
            $(".loadmore").fadeOut("slow");
        }
    });

    });
