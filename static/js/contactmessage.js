
    var etebar = document.getElementById("melicod_etebar")
    console.log(etebar.innerHTML)
    if ( etebar.innerHTML == 'false' ){ mymessage()}

    function mymessage(){
        Swal.fire({
              icon: 'هشدار',
              title: 'کد ملی وارد شده قبلا ثبت شده است',
              text: 'برای ورود یا بازیابی رمز از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/login/">kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk</a>'
})
    }
