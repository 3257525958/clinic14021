
    var etebar = document.getElementById("melicod_etebar");
    console.log(etebar.innerHTML);
    if ( etebar.innerHTML == 'false' ){ mymessage()}

    function mymessage(){
        Swal.fire({
              icon: 'هشدار',
              title: 'کد ملی وارد شده قبلا ثبت شده است',
              text: 'برای ورود یا بازیابی رمز از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/login/">ورود و بازیابی رمز</a>'
})
    }

    if ( etebar.innerHTML == 'empty')
    {
        Swal.fire({
            icon: 'warning',
            title: 'لطفا کد ملی را وارد کنید'
        })

    }
