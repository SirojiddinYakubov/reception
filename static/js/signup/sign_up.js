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
    var html = `<p>Hurmatli foydalanuvchi ! <a href="/">Onless.uz</a> tizimidan foydalanish bo'yicha yo'riqnoma bilan tanishib chiqing!</p>
<p style="text-align:left">1.<a href="/video/categories/">Videodarslar</a> bo'limidagi barcha videolar to'liq oxirigacha ko'rilishi lozim.</p>
<p style="text-align:left">2.Videodars ostida mavzuga oid testlar bo'lsa shu testlarga javob berishingiz kerak. (Eslatma: Video oxirigacha ko'rilmasa test ochilmaydi)</p>
<p style="text-align:left">3.<a href="/quiz/select-lang/">Test savollari</a>  bo'limiga o'tib <a href="/quiz/select-type/?lang=uz&type=T">mashg'ulot rejimi</a>da har bir biletni yechib chiqish (Eslatma: Agar mavjud biletdagi 10 ta savolga 10 ta javob to'g'ri berilmasa keyingi bilet ochilmaydi)</p>
<p style="text-align:left">4.<a href="/quiz/select-type/?lang=uz&type=T">Mashg'ulot rejimi</a>da barcha biletlar ko'rib chiqilgandan so'ng <a href="/quiz/select-type/?lang=uz&type=I">imtihon rejimi</a>da o'zingizni sinovdan o'tkazing!</p>

<p style="text-align:left">Sizning video ostidagi testlarga bergan javoblaringiz avtomaktab nazoratida bo'ladi.</p>
<p style="text-align:left">Guruh rahbaringiz esa sizning o'zlashtirish darajangizga qarab sizning nazariy bilimlaringizni baholab boradi. Siz uchun tushunarsiz savol yoki mavzularga oid savollar yuzaga kelsa telegramdagi <a href="https://t.me/onless_support">yordam guruh</a>imizga yozib qoldiring.  Sizga mutahasislar yordam berishadi. Agarda tizim borasida savol va takliflaringiz bo'lsa <a href="https://t.me/Sirojiddin_Yakubov">Sirojiddin Yakubov</a>ga yozib qoldiring.</p>
<p style="text-align:left">Agar siz mobil telefon orqali bizning tizimizdan foydalanayotgan bo'lsangiz chap tomondagi menyu yopiq holatda turadi. Menyuni ochish uchun ekranning eng yuqori chap tomonida 3 ta chiziqcha qo'yilgan. Menyuni ochib menyudagi har bir bo'lim bilan tanishib chiqing!</p>
<p style="text-align:left">Bizning tizimdan foydalanish uchun sizga yuborilgan login va parolning logini sizning passport seriyangiz, parolni esa tizimning o'zi avtomatik holatda 7 xonali sondan iborat raqam generatsiya qilib qo'yadi. Agarda siz o'zingiz uchun esda qolarli parol yaratmoqchi bo'lsangiz. Menyuga kirib <a href="/user/settings/">tahrirlash</a> bo'limidan parolni o'zgartiring va saqlashga bosing.</p>`
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
        if(IsConfirm){
            $('#accept').prop('checked', true)
            $('#agree').css('color', 'blue')
        }
    })
}