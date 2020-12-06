$(document).ready(function(){
    // Materialize
    $(".dropdown-trigger").dropdown({coverTrigger: false});
    $('.slider').slider({indicators: false});
    $('input#input_text, textarea#upload_description, textarea#comment_description').characterCounter();
    $('.collapsible').collapsible();
    $('select').formSelect();


    $(".dropdown-trigger1").dropdown({
        coverTrigger: false,
        alignment: "right"
        });
    $('.modal').modal();

// Select Validate function from the Code - Institute tutorial
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
// Load more function
    $(".card").slice(0, 4).show();
    $(".loadmore").on('click', function (e) {
        e.preventDefault();
        $(".card:hidden").slice(0, 4).slideDown();
        if ($(".card:hidden").length == 0) {
            $(".loadmore").fadeOut("slow");
        }
    });

    });
