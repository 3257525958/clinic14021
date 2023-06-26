
var newjobetebar = document.getElementById("newjobetebar");
        console.log("kjijujjhkjhkj");
        console.log(newjobetebar.innerHTML);
    if ( newjobetebar.innerHTML == 'ok' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'با موفقیت وارد شدید',
          showConfirmButton: false,
          timer: 2000
                 });
        setTimeout('redirectt()',500);
    }

    if ( newjobetebar.innerHTML == 'false') {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا فعالیت مورد نظرتان را وارد گنید'
        })
    }

    function redirectt() { window.location = "/"; }

function addjob() {
    document.getElementById('textobject').innerHTML = "تعریف فعالیت جدید";
    document.getElementById('regester').hidden = false;
    document.getElementById('regester').style.height = "200px";
    document.getElementsByClassName('newjob')[0].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[0].style.top = "130px";
    document.getElementById('regesterbuttoncancel').style.top = "130px";
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
    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[1].style.top = "130px";
    document.getElementById('regesterbuttoncancel').style.top = "130px";
    document.getElementsByClassName('newjob')[2].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = true;
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
}
function addemployee() {
    document.getElementById('textobject').innerHTML = "تعریف نیروی جدید برای فعالیتها";
    document.getElementById('regester').hidden = false;
    document.getElementsByClassName('newjob')[0].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[0].hidden = true;
    document.getElementsByClassName('newjob')[1].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[1].hidden = true;
    document.getElementsByClassName('newjob')[2].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[2].hidden = false;
    document.getElementsByClassName('regesterbuttonsave')[2].style.top = "130px";
    document.getElementById('regesterbuttoncancel').style.top = "130px";
    document.getElementsByClassName('newjob')[3].hidden = true;
    document.getElementsByClassName('regesterbuttonsave')[3].hidden = true;
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

