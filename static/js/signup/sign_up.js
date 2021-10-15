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

function instruction_sweet() {
    var html = `<p>1. Tizimda o'z shaxsiy telefon raqamingiz bilan ro'yhatdan o'tishingiz talab etiladi. Siz tomoningizdan kiritilganga har bir holat bo'yicha batafsil SMS xabarnoma yetkaziladi.</p>
<p style="text-align:left">2. Ma'lumotlarni kiritishda ma'lumotlar to'g'ri va aniq kiritilishi nazoratga oling. Noto'g'ri yoki noaniq kiritilgan ma'lumotlar uchun o'zingiz javobgar bo'lasiz. Agarda ushbu noto'g'ri ma'lumotlar asosida  siz davlat boji to'lasangiz, siz to'lagan to'lovlar qaytarilmaydi.</p>
<p style="text-align:left">3. Arizani chop etganingizdan so'ng, yana qayta tekshirishni unutmang.
<br><br>4. Hujjatlarni asl nusxasini o'zingiz tanlagan IIB YHXB RIB yoki YHXB TRIB'ga taqdim etish talab etiladi. </p>
<p style="text-align:left">5. YHXB RIB yoki TRIB tomonidan taqdim etiladigan vositalarni olish uchun arizachi va uning fuqarolik pasporti talab etilad</p>`

    var swalButtonTitle = 'Tanishib chiqdim!'
    Swal.fire({
        title: 'Tizimdan foydalanish uchun qo\'llanma',
        text: '',
        width: 900,
        html: html,
        showClass: {
            popup: 'animate__animated animate__fadeInDown',

        },
        hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
        },
        inputAttributes: {
            autocapitalize: 'off'
        },
        // {#customClass: 'swal-wide',#}
        showConfirmButton: true,
        focusConfirm: false,
        confirmButtonText: swalButtonTitle,
        confirmButtonColor: '#8b8989',
        allowOutsideClick: false,
        //  {#background: '#fff url(/images/trees.png)',#}
        //  {#backdrop: ``#}
        customClass: {
            backdrop: 'swal-wide',

        }

    }).then(function (IsConfirm) {
        if (IsConfirm) {
            $('#accept').prop('checked', true)
            $('#agree').css('color', 'blue')
        }
    })
}