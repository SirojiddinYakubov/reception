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

// Eterni false qiladi

function PressEnterFalse(e) {
    if (e.keyCode === 13 || e.which === 13) {
        e.preventDefault();
        return false;
    }
}


function isDate(ExpiryDate) {
    var objDate,  // date object initialized from the ExpiryDate string
        mSeconds, // ExpiryDate in milliseconds
        day,      // day
        month,    // month
        year;     // year
    // date length should be 10 characters (no more no less)
    if (ExpiryDate.length !== 10) {
        return false;
    }
    // third and sixth character should be '/'
    if (ExpiryDate.substring(2, 3) !== '.' || ExpiryDate.substring(5, 6) !== '.') {
        return false;
    }
    // extract month, day and year from the ExpiryDate (expected format is mm/dd/yyyy)
    // subtraction will cast variables to integer implicitly (needed
    // for !== comparing)
    month = ExpiryDate.substring(0, 2) - 1; // because months in JS start from 0
    day = ExpiryDate.substring(3, 5) - 0;
    year = ExpiryDate.substring(6, 10) - 0;
    // test year range
    if (year < 1000 || year > 3000) {
        return false;
    }
    // convert ExpiryDate to milliseconds
    mSeconds = (new Date(year, month, day)).getTime();
    // initialize Date() object from calculated milliseconds
    objDate = new Date();
    objDate.setTime(mSeconds);
    // compare input date and parts from Date() object
    // if difference exists then date isn't valid
    if (objDate.getFullYear() !== year ||
        objDate.getMonth() !== month ||
        objDate.getDate() !== day) {
        return false;
    }
    // otherwise return true
    return true;
}

function checkDate(){
    // define date string to test
    var ExpiryDate = document.getElementById(' ExpiryDate').value;
    // check date and print message
    if (isDate(ExpiryDate)) {
        alert('OK');
    }
    else {
        alert('Invalid date format!');
    }
}

