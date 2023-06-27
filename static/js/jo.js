
var newjobetebar = document.getElementById("newjobetebar");
var deletjobetebar = document.getElementById("deletjob");
var lenjob = document.getElementById('lenjob');
var useretebar = document.getElementById('useretebar');
var employeeetebar = document.getElementById('employeeetebar');
var employeemessage = document.getElementById('employeemessage');
var    j = ( lenjob.innerHTML  * 19 ) + 100 ;
    console.log(j);

    if ( newjobetebar.innerHTML == 'ok' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'فعالیت مورد نظر با موفقیت ثبت شد',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }

    if ( newjobetebar.innerHTML == 'false') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا فعالیت مورد نظرتان را وارد گنید'
        })
    }
    if ( newjobetebar.innerHTML == 'repeat') {
        Swal.fire({
            icon: 'warning',
            title: 'فعالیت وارد شده تکراری است لطفا فعالیت جدید وارد کنید'
        })
    }

    function redirectt() { window.location = "/"; }

    if ( deletjobetebar.innerHTML == 'delet' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'فعالیت مورد نظر با موفقیت حذف گردید',
          showConfirmButton: false,
          timer: 2000
                 });
    }


        if ( deletjobetebar.innerHTML == 'ok') {
        Swal.fire({
            icon: 'warning',
            title: 'یک فعالیت برای حذف انتخاب کنید'
        })
    }

    if ( useretebar.innerHTML == 'false' ){
                Swal.fire({
              icon: 'هشدار',
              title: 'این کد ملی تاکنون ثبت نام نکرده است',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
});
    }
        if ( employeeetebar.innerHTML == 'ok') {
        Swal.fire({
            icon: 'warning',
            title: 'یک فعالیت انتخاب کنید'
        })
    }
    var m = employeemessage.innerHTML;
    if ( employeeetebar.innerHTML == 'addmployee' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'با موفقیت ثبت شد'+m,
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',1000);
    }



function addjob() {
    document.getElementById('textobject').innerHTML = "تعریف فعالیت جدید";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = "260px";
    document.getElementsByClassName('newjob')[0].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[0].style.top = "190px";
    document.getElementById('regesterbuttoncancel').style.top = "190px";
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
}
function deletjob() {
    document.getElementById('textobject').innerHTML = "حذف فعالیت از لیست";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = j+70+"px";
    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[1].style.top = j+"px";
    document.getElementById('regesterbuttoncancel').style.top = j+"px";
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
}
function addemployee() {
    document.getElementById('textobject').innerHTML = "تعریف نیروی جدید برای فعالیتها";
    document.getElementById('regester').style.height = j+150+"px";
    document.getElementById('regester').hidden = false;
    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[2].style.top = j+50+"px";
    document.getElementById('regesterbuttoncancel').style.top = j+50+"px";
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
    document.getElementsByClassName('inputclass')[2].style.top = j+"px";
}
function deletemployee() {
    document.getElementById('textobject').innerHTML = "حذف نیرو از لیست ";
    document.getElementById('regester').hidden = false;
    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[3].style.top = "130px";
    document.getElementById('regesterbuttoncancel').style.top = "130px";
}

