$(document).ready(function () {

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;

    $(".next").click(function () {

        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

//Add Class Active
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

//show the next fieldset
        next_fs.show();
//hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function (now) {
// for making fielset appear animation
                opacity = 1 - now;

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                next_fs.css({'opacity': opacity});
            },
            duration: 600
        });
    });

    $(".previous").click(function () {

        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();

//Remove class active
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

//show the previous fieldset
        previous_fs.show();

//hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function (now) {
// for making fielset appear animation
                opacity = 1 - now;

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                previous_fs.css({'opacity': opacity});
            },
            duration: 600
        });
    });

    $('.radio-group .radio').click(function () {
        $(this).parent().find('.radio').removeClass('selected');
        $(this).addClass('selected');
    });

    $(".submit").click(function () {
        return false;
    })

})


// get csrftoken from cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//   function getCookie(name) {
//      var cookieValue = null;
//       if (document.cookie && document.cookie !== '') {
//          var cookies = document.cookie.split(';');
//          for (var i = 0; i < cookies.length; i++) {
//              var cookie = jQuery.trim(cookies[i]);
// Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                  break;
//              }
//          }
//      }
//      return cookieValue;
//    }

//     var csrftoken = getCookie('csrftoken');

//     $.ajaxSetup({
//        beforeSend: function (xhr) {
//            xhr.setRequestHeader('X-CSRFToken', csrftoken)
//        }
//    })