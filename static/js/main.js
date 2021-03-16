// Ruxsat berilgan lotin va kiril bosh harflar, raqamlar
function PassportInputFilter(e) {
    var ew = e.which

    if (32 <= ew && ew <= 47) {
        e.preventDefault()
    } else if (58 <= ew && ew <= 64) {
        e.preventDefault()
    } else if (91 <= ew && ew <= 126) {
        $.notifyDefaults({
            type: 'danger',
            allow_dismiss: false,
        })
        $.notify({
            icon: 'glyphicon glyphicon-star',
            message: '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-exclamation" fill="currentColor" xmlns="http://www.w3.org/2000/svg">\n' +
                '  <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>\n' +
                '  <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>\n' +
                '</svg> Faqat bosh harflar kiriting!'
        })
        e.preventDefault()
    } else if (1072 <= ew && ew <= 1105) {
        $.notifyDefaults({
            type: 'danger',
            allow_dismiss: false,
        })
        $.notify({
            icon: 'glyphicon glyphicon-star',
            message: '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-exclamation" fill="currentColor" xmlns="http://www.w3.org/2000/svg">\n' +
                '  <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>\n' +
                '  <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>\n' +
                '</svg> Faqat bosh harflar kiriting!'
        })
        e.preventDefault()
    }
}

// Ruxsat berilgan lotin va kiril bosh harflar
function OnlyBigLetter(e) {
    var ew = e.which

    if (32 <= ew && ew <= 64) {
        e.preventDefault()
    } else if (91 <= ew && ew <= 126) {
        $.notifyDefaults({
            type: 'danger',
            allow_dismiss: false,
        })
        $.notify({
            icon: 'glyphicon glyphicon-star',
            message: '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-exclamation" fill="currentColor" xmlns="http://www.w3.org/2000/svg">\n' +
                '  <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>\n' +
                '  <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>\n' +
                '</svg> Faqat bosh harflar kiriting!'
        })
        e.preventDefault()
    } else if (1072 <= ew && ew <= 1105) {
        $.notifyDefaults({
            type: 'danger',
            allow_dismiss: false,
        })
        $.notify({
            icon: 'glyphicon glyphicon-star',
            message: '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-exclamation" fill="currentColor" xmlns="http://www.w3.org/2000/svg">\n' +
                '  <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>\n' +
                '  <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>\n' +
                '</svg> Faqat bosh harflar kiriting!'
        })
        e.preventDefault()
    }
}


// Ruxsat berilgan Lotin va rus bosh harflari va probel

function CustomInputFilter(e) {

    var ew = e.which

    if (33 <= ew && ew <= 64) {
        e.preventDefault()
    } else if (91 <= ew && ew <= 126) {
        $.notifyDefaults({
            type: 'danger',
            allow_dismiss: false,
        })
        $.notify({
            icon: 'glyphicon glyphicon-star',
            message: '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-exclamation" fill="currentColor" xmlns="http://www.w3.org/2000/svg">\n' +
                '  <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>\n' +
                '  <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>\n' +
                '</svg> Faqat bosh harflar kiriting!'
        })
        e.preventDefault()
    } else if (1072 <= ew && ew <= 1105) {
        $.notifyDefaults({
            type: 'danger',
            allow_dismiss: false,
        })
        $.notify({
            icon: 'glyphicon glyphicon-star',
            message: '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-exclamation" fill="currentColor" xmlns="http://www.w3.org/2000/svg">\n' +
                '  <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>\n' +
                '  <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>\n' +
                '</svg> Faqat bosh harflar kiriting!'
        })
        e.preventDefault()
    }
}

// Ruxsat berilgan katta va kichik lotin va kril harflar, probel

function NameInputFilter(e) {
    var ew = e.which;

    if (33 <= ew && ew <= 38)
        return false;
    if (40 <= ew && ew <= 64)
        return false;
    if (91 <= ew && ew <= 96)
        return false;
    if (123 <= ew && ew <= 126)
        return false;
    if (186 <= ew && ew <= 222)
        return false;
    return true;
}

// Inputdagi yozishlar sonini cheklaydi

function InputMaxLength() {
    var $this = $(this);
    var maxlength = $this.attr('max').length;
    var value = $this.val();
    if (value && value.length >= maxlength) {
        $this.val(value.substr(0, maxlength));
    }
}

// Enterni false qiladi

function PressEnterFalse(e) {
    if (e.keyCode === 13 || e.which === 13) {
        e.preventDefault();
        return false;
    }
}


function parseDate(value) {
    var date = value.split("-");
    var y = parseInt(date[0], 10),
        m = parseInt(date[1], 10),
        d = parseInt(date[2], 10);
    if (y != NaN && m != NaN && d != NaN) {
        return y
    }
    // return `${d}.${m}.${y}`

    // return new Date(y, m - 1, d);
}

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


$('#id').on('click', function () {

    var pdf = new jsPDF('p', 'pt', 'letter');
    // source can be HTML-formatted string, or a reference
    // to an actual DOM element from which the text will be scraped.
    source = $('#id')[0];

    // we support special element handlers. Register them with jQuery-style
    // ID selector for either ID or node name. ("#iAmID", "div", "span" etc.)
    // There is no support for any other type of selectors
    // (class, of compound) at this time.
    specialElementHandlers = {
        // element with id of "bypass" - jQuery style selector
        '#bypassme': function (element, renderer) {
            // true = "handled elsewhere, bypass text extraction"
            return true
        }
    };
    margins = {
        top: 80,
        bottom: 60,
        left: 40,
        width: 1000
    };
    // all coords and widths are in jsPDF instance's declared units
    // 'inches' in this case
    pdf.fromHTML(
        source, // HTML string or DOM elem ref.
        margins.left, // x coord
        margins.top, { // y coord
            'width': margins.width, // max width of content on PDF
            'elementHandlers': specialElementHandlers
        },

        function (dispose) {
            // dispose: object with X, Y of the last line add to the PDF
            //          this allow the insertion of new lines after html
            pdf.save("To'lov.pdf");
        }, margins);


})

// suratni javascript orqali joyida ochib ko'rish'

// $('#accountStatementPhoto').on('change', function (event) {
//                 var files = event.target.files; //FileList object
//                 for (var i = 0; i < files.length; i++) {
//                     var file = files[i];
//
//                     //Only pics
//                     if (!file.type.match('image'))
//                         continue;
//                     var picReader = new FileReader();
//                     picReader.addEventListener("load", function (event) {
//                         var picFile = event.target;
//                         //  var div = document.createElement("div");
//                         $('#accountStatementPhotoPreview label').hide()
//                         $('#accountStatementThumbnail').show()
//                         $('#accountStatementRemove').show()
//                         $('#accountStatementThumbnail').attr('src', picFile.result)
//                         $('#accountStatementPhotoError').hide()
//                         // result.innerHTML = "<img style='width: 150px; height: auto' id='thumbnail' src='" + picFile.result + "'" +
//                         //   "title='Image'/><span  id='remove'>O'chirish</span>";
//                         //  result.insertBefore(div, null);
//                         $("#accountStatementRemove").click(function () {
//                             $('#accountStatementPhotoPreview label').show()
//                             $('#accountStatementThumbnail').hide()
//                             $('#accountStatementRemove').hide()
//                             $('#accountStatementPhotoError').show()
//                         });
//                     });
//                     //Read the image
//                     picReader.readAsDataURL(file);
//                 }
//             })


// var accountStatementPhoto = $('#accountStatementPhoto')[0].files[0];
//
//
// fd.append('accountStatementPhoto', accountStatementPhoto);


// html template

// < div
// className = "col-12 col-md-6 col-sm-6 col-lg-6 col-xl-6 mt-2" >
//     < div
// id = "accountStatementPhotoPreview" >
//     < label
// className = "not_copy"
// htmlFor = "accountStatementPhoto" > Xisob
// ma
// 'lumotnoma
// suratini
// yuklang < /label>
//
// <input type="file" name="photo" hidden
//        id="accountStatementPhoto" accept=".jpg, .jpeg, .png, .gif"/>
//
// <img style='width: 120px; height: auto;display: none' id='accountStatementThumbnail'
//      src="" title='Image'/>
// <span style="display: none" id='accountStatementRemove'>O'chirish</span>
// </div>
// <p id="accountStatementPhotoError"
// style="font-size: smaller; margin-top: 0; padding-top: 0; margin-bottom: 0; display: none; float: left"
// className="form-text text-danger">Xisob ma'lumotnoma surati yuklanmagan</p>
// </div>


var dateReg = /^(0?[1-9]|[12][0-9]|3[01])[./-](0?[1-9]|1[012])[./-]\d{4}$/

$(function () {
    $(".datepicker").datepicker({
        dateFormat: "dd.mm.yy",
        // minDate: '-150M',
        // maxDate: '+5M',
        defaultDate: '01.01.1990',
        // value: "7/11/2011",
        showButtonPanel: true,
        numberOfMonths: 1,
        // showOn: '',
        // startDate: "-130M",
        //endDate: "+30d",
        //currentText: 'Today',
        autoclose: true,
        changeMonth: true,
        changeYear: true,


        //yakshanbalarni chiqarish
        // beforeShowDay: function (date) {
        //     var day = date.getDay();
        //     return [(day !== 0), ''];
        // },

        onClose: function () {
            if ($(this).val().match(dateReg)) {
                $(this).css("border-bottom", "2px solid green")
            } else {
                $(this).css("border-bottom", "2px solid red")
            }
        }
    })
    $(".datepicker").datepicker('setDate', new Date());
})

$('.datepicker_icon').on('click', function () {
    $('.datepicker').datepicker('show')
})

$('.datepicker').on('keypress', function (e) {
    return false
})

// $(document).on('keypress', '#body_type, #body_number, #chassis_number, #engine_number, #made_year,#additionality, #color, #cert_seriya, #cert_number', function (e) {
//     if (e.target.value !== '') {
//         $(e.target).css("border-bottom", "2px solid green")
//     } else {
//         $(e.target).css("border-bottom", "2px solid red")
//     }
// })

//div render to pdf

// $('#payment_render_pdf').on('click', function () {
//     var pdf = new jsPDF('p', 'pt', 'letter');
//     source = $('#render_div')[0];
//     specialElementHandlers = {
//         '#bypassme': function (element, renderer) {
//             return true
//         }
//     };
//     margins = {
//         top: 80,
//         bottom: 60,
//         left: 40,
//         width: 1000
//     };
//     pdf.fromHTML(
//         source, // HTML string or DOM elem ref.
//         margins.left, // x coord
//         margins.top, { // y coord
//             'width': margins.width, // max width of content on PDF
//             'elementHandlers': specialElementHandlers
//         },
//         function (dispose) {
//             pdf.save("To'lov.pdf");
//         }, margins);
// })


// $(window).bind('hashchange', function () {
//     if (window.location.hash === '#step-3') {
//         if ($('#step-3').data('transition') === false) {
//             window.location.hash = '#step-1'
//         }
//     } else if (window.location.hash === '#step-2') {
//         if ($('#step-2').data('transition') === false) {
//             window.location.hash = '#step-1'
//         }
//     }
// })

// Jquery validation metod

// jQuery.validator.addMethod("noSpace", function (value, element) {
//     return value == '' || value.trim().length != 0;
// }, "Iltimos, bo'sh joy qoldirmang!");
// jQuery.validator.addMethod("customEmail", function (value, element) {
//     return this.optional(element) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(value);
// }, "Iltimos, to'g'ri elektron pochta manzilini kiriting!");
// $.validator.addMethod("alphanumeric", function (value, element) {
//     return this.optional(element) || /^\w+$/i.test(value);
// }, "Faqat harf va raqam kiriting!");


// $("#save_car_form").validate()
//
// $("#chassis_number").rules("add", {
//     required: true,
//     messages: {
//         required: "Shassi raqami kiritilmagan!",
//     })

function errorFunction() {

    $.notifyDefaults({
        type: 'danger',
        allow_dismiss: false,
        z_index: '9999'
    })
    $.notify({
        icon: 'glyphicon glyphicon-star',
        message: '<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-patch-exclamation" fill="currentColor" xmlns="http://www.w3.org/2000/svg">\n' +
            '  <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>\n' +
            '  <path fill-rule="evenodd" d="M10.273 2.513l-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>\n' +
            '</svg> Xatolik yuz berdi! Sahifani yangilab qayta urinib ko\'ring'
    })
}