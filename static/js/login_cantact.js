    var vorod_etebar = document.getElementById("vorod_etebar")
    console.log(vorod_etebar.innerHTML)
    if ( vorod_etebar.innerHTML == 'true' ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'با موفقیت وارد شدید',
          showConfirmButton: false,
          timer: 1500
                 });
        window.open('http://drmahdiasadpour.ir','_self');
}


    if ( vorod_etebar.innerHTML == 'false_in_paswoord' ){
        Swal.fire({
            icon: 'هشدار',
            title: 'رمز اشتباه است',
            text: 'برای ورود یا بازیابی رمز از لینک زیر استفاده کنید',
            footer: '<a href="/cantact/ignor/">فراموشی رمز</a>'
})
    }


    if ( vorod_etebar.innerHTML == 'false' ){
                Swal.fire({
              icon: 'هشدار',
              title: 'این کد ملی تاکنون ثبت نام نکرده است',
              text: 'برای ثبت نام از لینک زیر استفاده کنید',
              footer: '<a href="/cantact/addcontact/">ثبت نام </a>'
})
    }
